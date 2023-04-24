from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializers, DockerComposeSerializers, NginxTemplateSerializers
from cdtool.models import Service, DockerComposeTemplate, NginxTemplate
# Create your views here.


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializers

    def get_queryset(self):
        return Service.objects.all()

class DockerComposeViewSet(viewsets.ModelViewSet):
    queryset = DockerComposeTemplate.objects.all().order_by('name')
    serializer_class = DockerComposeSerializers

class NginxTemplateViewSet(viewsets.ModelViewSet):
    queryset = NginxTemplate.objects.all().order_by('name')
    serializer_class = NginxTemplateSerializers
