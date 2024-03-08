from django.db import models

# Create your models here.
class user_master(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=20)
    contact=models.CharField(max_length=12,blank=True)
    image=models.ImageField(upload_to='images')
    rol_name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

class contact_master(models.Model):
    name=models.CharField(max_length=40)    
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    def __str__(self):
        return self.name 
    

class test_employee(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=10)
    email=models.EmailField(max_length=20, unique=True)
    contact=models.CharField(max_length=12,blank=True)
    image=models.ImageField(upload_to='images')
    address=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updates_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.firstname