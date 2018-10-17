from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required(login_url='/accounts/login/')
def home(request):
    projects=Project.objects.all()
    return render(request,'index.html',{'projects':projects})
