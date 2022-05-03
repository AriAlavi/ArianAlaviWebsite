from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import FileResponse
from django.http import HttpResponseRedirect
from main.models import *

def home(request):
    context = {
        "projects" : Project.objects.all(),
        "skills" : Skill.objects.all(),
    }
    return render(request, "main/home.html", context)

def interests(request):
    return render(request, "main/interests.html")

def contact(request):
    return render(request, "main/contact.html")

def resumeFile(request):
    filepath = staticfiles_storage.path("main/resume.pdf")
    return FileResponse(open(filepath, "rb"))

def resume(request):
    return render(request, "main/resumeHTML.html")
