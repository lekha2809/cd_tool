from django.contrib import admin
from .models import Service, DockerComposeTemplate, NginxTemplate
# Register your models here.
class ServiceView(admin.ModelAdmin):
    list_display = (
        'name', 'bitbucket_slug', 'cd_name', 'type', 'image_name', 'deploy_template', 'service_port', 'nginx_template',
        'nginx_port', 'create_at', 'active')
    search_fields = ['name', 'bitbucket_slug', 'service_port', 'nginx_port']
    list_filter = ['type', 'active']
    list_editable = ['active']


class DockerComposeTemplateView(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class NginxTemplateView(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Service, ServiceView)
admin.site.register(DockerComposeTemplate, DockerComposeTemplateView)
admin.site.register(NginxTemplate, NginxTemplateView)
