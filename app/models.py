from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first    = models.CharField(max_length=64)
    last     = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    email    = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    age      = models.IntegerField()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    description = models.TextField()

class Post(models.Model):
    text=models.TextField() 
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey( Blog,related_name="posts" )
    user = models.ForeignKey( User,related_name="posts" )