from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("interests/", interests, name="interests"),
    path("contact/", contact, name="contact"),
    path('resume/', resume, name="resume")
]