from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import User

from django.contrib.messages import get_messages

def showRegister(request):
    return render(request,"register.html");

def register(request):
    User.objects.validate(request);
    if len(get_messages(request)) < 1:
        User.objects.register(request);
    return redirect("/users");