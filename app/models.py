from __future__ import unicode_literals
from django.db import models

from django.contrib import messages
import bcrypt

class UserManager(models.Manager):
    def validate(self,request):
        if len(request.POST["first"]) < 1:
            messages.add_message(request,messages.ERROR,"First name must be between 2-64")
        if len(request.POST["last"]) < 1:
            messages.add_message(request,messages.ERROR,"Last name must be between 2-64");
        if len(request.POST["email"]) < 1:
            messages.add_message(request,messages.ERROR,"Email must be between 2-64");
        if len(request.POST["password"]) < 1:
            messages.add_message(request,messages.ERROR,"Password must be between 2-64");   
        if len(request.POST["age"]) < 1:
            messages.add_message(request,messages.ERROR,"Email must be between 2-64");

    def register(self,request):
        pw = bcrypt.hashpw( request.POST["password"].encode("utf-8") ,bcrypt.gensalt(8));

        self.create(
            first=request.POST["first"],
            last=request.POST["last"],
            email=request.POST["email"],
            password=pw,
            age=request.POST["age"],
        );

class User(models.Model):
    first    = models.CharField(max_length=64)
    last     = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    email    = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    age      = models.IntegerField()
    objects  = UserManager()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    description = models.TextField()

class Post(models.Model):
    text=models.TextField() 
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey( Blog,related_name="posts",on_delete=models.CASCADE )
    user = models.ForeignKey( User,related_name="posts",on_delete=models.CASCADE )























