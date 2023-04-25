from django.db import models
from yamlfield.fields import YAMLField


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

# Create your models here.
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

class ActiveServiceOnEnv(models.Model):
    service = models.ForeignKey(Service)
    env = models.ForeignKey(DeployEnvironment)
    active = models.BooleanField(blank=True, default=False)