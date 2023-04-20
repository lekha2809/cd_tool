from django.shortcuts import render

# Create your views here.

def docker(request):
    return render(request, 'docker/docker.html')

def history(request):
    return render(request, 'docker/history.html')

def login(request):
    return render(request, 'docker/login_page.html')