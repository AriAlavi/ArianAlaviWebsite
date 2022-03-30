from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def interests(request):
    return render(request, "main/interests.html")

def contact(request):
    return render(request, "main/contact.html")