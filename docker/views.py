from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def docker(request):
    return render(request, 'docker/basic.html')

def history(request):
    return render(request, 'docker/history.html')

def login(request):
    return render(request, 'docker/login_page.html')

def deploy(request):
    return HttpResponse(content='success', status=200)

