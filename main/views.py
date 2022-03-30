from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import FileResponse

def home(request):
    return render(request, "main/home.html")

def interests(request):
    return render(request, "main/interests.html")

def contact(request):
    return render(request, "main/contact.html")

def resume(request):
    filepath = staticfiles_storage.path("main/resume.pdf")
    return FileResponse(open(filepath))