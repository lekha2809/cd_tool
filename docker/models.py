from __future__ import unicode_literals

# from django.db import models

# Create your models here.


from django.db import models
from yamlfield.fields import YAMLField

#from fimplus.utils.convertion import get_time_from_string


class DockerComposeTemplate(models.Model):
    """
    Docker compose
    """
    name = models.CharField(max_length=255, default='default', unique=True)
    docker_compose_template = YAMLField(null=True)

    def __str__(self):
        return self.name

class NginxTemplate(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    """
        Service map to each microservice
    """
    name = models.CharField(max_length=255)
    bitbucket_slug = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    cd_name = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, default='api')
    image_name = models.CharField(max_length=255, null=True)
    nginx_port = models.IntegerField(default=80, null=True, blank=True)
    service_port = models.IntegerField(default=8080, null=True, blank=True)
    # docker_compose_template = YAMLField(null=True)
    deploy_template = models.ForeignKey(DockerComposeTemplate,on_delete=models.CASCADE, null=True)
    scheduler_rule = models.CharField(max_length=255, null=True, blank=True)
    nginx_template = models.ForeignKey(NginxTemplate,on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(blank=True, default=False)

    def get_image_name(self):
        if not self.image_name:
            return self.bitbucket_slug
        else:
            return self.image_name

    def get_service_type(self):
        return self.type

    def get_deploy_template(self):
        return self.deploy_template.docker_compose_template

    def get_service_name(self):
        return self.name


    def get_cd_name(self):
        return self.cd_name

    def __str__(self):
        return self.name

    def get_nginx_port(self, env_name):
        """
        :param env_name: stag, sand, prod
        :return:
        """

        # if env_name == 'sand':
        # port = self.nginx_port + 10000
        # return port
        # else:
        # return self.nginx_port

        return self.nginx_port

    def get_rsyslog_tag(self, env):
        return '%s_%s' % (self.name, env)


class DeployHistory(models.Model):
    task_id = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    commit_tag = models.CharField(max_length=255, null=True)
    docker_compose = YAMLField(null=True)
    scheduler_info = YAMLField(null=True)
    scale = models.IntegerField(null=True)
    env = models.CharField(max_length=255, null=True)
    deploy_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='success')
    desc = models.TextField(max_length=255, null=True)

    def convert_to_dict(self):
        json_data = {}
        json_data['cd_name'] = self.service.cd_name
        json_data['commit_tag'] = self.commit_tag
        json_data['env'] = self.env
        json_data['deploy_time'] = self.deploy_time
        json_data['status'] = self.status
        json_data['desc'] = self.desc

        return json_data

class DeployEnvironment(models.Model):
    name = models.CharField(max_length=255)
    app_env = models.CharField(max_length=255)
    swarm_manager = models.CharField(max_length=255)
    more_info = YAMLField(null=True)

    def __str__(self):
        return self.name

    def get_docker_host(self):
        return self.swarm_manager

    def get_node_env_environment(self):
        return self.app_env

    def get_rsys_log_address_docker(self):
        return self.more_info['log_docker']

    def get_rsys_log_address_nginx(self):
        return self.more_info['log_nginx']

    def get_dns_list(self):
        return self.more_info['dns']

    def send_slack(self):
        if 'send_slack' in self.more_info:
            return self.more_info['send_slack']
        else:
            return False

class Instance(models.Model):
    container_name = models.CharField(max_length=255, null=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE, null=True)
    public_port = models.IntegerField(null=True, default=0, blank=True)
    docker_node = models.CharField(max_length=255, null=True, blank=True)
    scheduler_rule = models.CharField(max_length=255, null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    more_info = models.TextField(max_length=255, null=True, blank=True)
    image_tag = models.CharField(max_length=255, null=True, blank=True)
    env = models.ForeignKey(DeployEnvironment,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, null=True, blank=True, default='unknown')

    def get_name_container(self):
        return '%s_%s' % (self.container_name, self.env.name)

    def ignore_expose_port(self):
        if self.service.type == 'worker':
            return True
        return False

    def get_host_name_container(self):
        return ('%s-%s' % (self.container_name, self.env.name)).replace('_', '-')

    class Meta:
        unique_together = (("docker_node", "public_port", "env"), ("container_name", "env"))


class ActiveServiceOnEnv(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    env = models.ForeignKey(DeployEnvironment, on_delete=models.CASCADE)
    active = models.BooleanField(blank=True, default=False)
