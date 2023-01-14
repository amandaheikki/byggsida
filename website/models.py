from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models
from django.urls import reverse




# Create your models here.

class StartModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="")
    content = models.TextField()
    contact = models.TextField()
    about = models.TextField()
    services = models.TextField()
    start_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    about_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    contact_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    services_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    def __str__(self):
        return self.title


class AboutModel(models.Model):
    title = models.CharField(max_length=200)
    topcontent = models.TextField()
    box1Title = models.CharField(max_length=200, null=True)
    box2Title = models.CharField(max_length=200, null=True)
    box1Des = models.TextField(null=True)
    box2Des = models.TextField(null=True)
    box1_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    box2_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    def __str__(self):
        return self.title


class ServiceModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    topcontent = models.TextField()
    box1Title = models.CharField(max_length=200, null=True)
    box2Title = models.CharField(max_length=200, null=True)
    box1_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    box2_img = models.ImageField(null=True, blank=True, upload_to="images/%y")
    box1Des = models.TextField(null=True)
    box2Des = models.TextField(null=True)
    def __str__(self):
        return self.title

class EstimateModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title

class ContactModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title

class ReferenceModel(models.Model):
    caption = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="images/%y", null=True)
    def __str__(self):
        return self.caption





