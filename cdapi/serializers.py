from rest_framework import serializers
from cdtool.models import Service, DockerComposeTemplate, NginxTemplate

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'bitbucket_slug', 'create_at', 'cd_name', 'type', 'image_name', 'nginx_port', 
                  'service_port', 'deploy_template', 'scheduler_rule', 'nginx_template', 'active')

class DockerComposeSerializers(serializers.ModelSerializer):
    class Meta:
        model = DockerComposeTemplate
        fields = ('name', 'docker_compose_template')

class NginxTemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = NginxTemplate
        fields = ('name', 'template')