import imp
from django.contrib import admin
from .models import *


#Register your models here.

myModels = [StartModel, AboutModel, ServiceModel, EstimateModel, ContactModel, ReferenceModel]
admin.site.register(myModels)
