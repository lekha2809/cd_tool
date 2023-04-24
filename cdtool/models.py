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