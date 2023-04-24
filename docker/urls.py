from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.docker, name='docker'),
    path('history/', views.history, name='history'), 
    path("accounts/", include("django.contrib.auth.urls")),
    re_path("^api/deploy/$", views.deploy, name='deploy')
]
