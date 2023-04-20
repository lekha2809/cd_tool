from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.docker, name='docker'),
    path('history/', views.history, name='history'), 
    
]
