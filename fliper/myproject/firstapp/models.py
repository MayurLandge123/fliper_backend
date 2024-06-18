from django.db import models

from django.contrib.auth.models import User

class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,default='null')
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    creat_at=models.DateField()

class Community(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE,related_name='+')
    user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='+')
    role = models.ForeignKey(Role,  on_delete=models.CASCADE,related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    community = models.ForeignKey(Community,  on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='+')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    id= models.AutoField(primary_key=True)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE,related_name='+')
    user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='+')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
