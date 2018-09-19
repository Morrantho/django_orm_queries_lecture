from __future__ import unicode_literals
from django.shortcuts import render,redirect
from models import User

def showRegister(request):
    return render(request,"register.html");

def register(request):
    a = request.POST["first"];
    b  = request.POST["last"];
    c  = request.POST["email"];
    d  = request.POST["password"];
    e  = request.POST["age"];

    User.objects.create(
        first=a,
        last=b,
        email=c,
        password=d,
        age=e
    );

    return redirect("/users");