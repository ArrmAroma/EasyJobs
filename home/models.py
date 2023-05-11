from distutils.command.upload import upload
from email.policy import default
from operator import mod
from turtle import position
from django.db import models
from django.contrib.auth.models import User





from django.core.exceptions import ValidationError
from mongoengine import Document, StringField, ImageField
from setuptools import Require
# Create your models here.
# from django.contrib.auth.models import AbstractUser

def validate_file_extension(value):
    if not value.name.endswith('.jpg') and not value.name.endswith('.png'):
        raise ValidationError("File must be .jpg or .png")

class Company(models.Model):
    compname                    = models.CharField(max_length=120)
    password                    = models.CharField(max_length=32)
    category                    = models.CharField(max_length=64)
    phone                       = models.CharField(max_length=20)
    email                       = models.CharField(max_length=120)
    address                     = models.CharField(max_length=255)
    description                 = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="company", blank=True, null=True, validators=[validate_file_extension])
    # user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Member(models.Model):
    username                = models.CharField(max_length=120)
    password                = models.CharField(max_length=32)
    name_th                 = models.CharField(max_length=120)
    name_eng                = models.CharField(max_length=120)
    birth_day               = models.CharField(max_length=64)
    sex                     = models.CharField(max_length=10)
    nationality             = models.CharField(max_length=32)
    religion                = models.CharField(max_length=64)
    phone                   = models.CharField(max_length=10)
    email                   = models.CharField(max_length=120)
    school                  = models.CharField(max_length=120)
    education_level         = models.CharField(max_length=64)
    faculty                 = models.CharField(max_length=120)
    major                   = models.CharField(max_length=120)
    education_category      = models.CharField(max_length=64)
    state                   = models.CharField(max_length=32)
    year                    = models.CharField(max_length=10)
    gpa                     = models.CharField(max_length=10)
    application_form        = models.ForeignKey(Company,on_delete=models.CASCADE)
    

class Job(models.Model):    
    compname   = models.CharField(max_length=100)
    position  = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    salary = models.IntegerField()
    quantity = models.IntegerField()
    type = models.CharField(max_length=32)
    logo = models.ImageField(upload_to="company", blank=True, null=True, validators=[validate_file_extension])
    gpa = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    property = models.CharField(max_length=500)
    welfare = models.CharField(max_length=500)
    experience = models.CharField(max_length=32)
    posted_date = models.DateTimeField()
    working_time = models.CharField(max_length=120)
    

class JobApply(models.Model):
    compname   = models.CharField(max_length=100)
    position     = models.CharField(max_length=64)
    members    = models.CharField(max_length=100)
    apply_date = models.DateTimeField(auto_now_add=True)
    member_id  = models.IntegerField()
    job_id     = models.IntegerField()

    




class Image(models.Model):
    name_Image = models.CharField(max_length=120)
    image = models.ImageField(validators=[validate_file_extension]) #required=True







