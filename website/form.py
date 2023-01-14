from dataclasses import fields
from pyexpat import model
from weakref import ref
from django import forms
from .models import StartModel, AboutModel, ServiceModel, EstimateModel, ReferenceModel

from .models import *

#STARTPAGE
class updateStartPage(forms.ModelForm):
    class Meta:
        model = StartModel
        fields = ["title", "content", "start_img"]

class updateStartPageContent1(forms.ModelForm):
    class Meta:
        model = StartModel
        fields = ["about", "about_img"]

class updateStartPageContent2(forms.ModelForm):
    class Meta:
        model = StartModel
        fields = ["contact", "contact_img"]

class updateStartPageContent3(forms.ModelForm):
    class Meta:
        model = StartModel
        fields = ["services", "services_img"]


#ABOUTPAGE
class updateAboutPage(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = ["title", "topcontent"]      

class updateAboutContent1(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = ["box1Title", "box1Des", "box1_img"]   

class updateAboutContent2(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = ["box2Title", "box2Des", "box2_img"]  
  
#SERVICES-PAGE
class updateServiceHeading(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = ["title", "topcontent"]    

class updateServiceContent1(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = ["box1Title", "box1Des", "box1_img"]  

class updateServiceContent2(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = ["box2Title", "box2Des", "box2_img"]  


#ESTIMATE-PAGE
class updateEstimateHeading(forms.ModelForm):
    class Meta:
        model = EstimateModel
        fields = ["title", "content"]

#CONTACT-PAGE
class updateContactHeading(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["title", "content"]

#REFERENCES
class addImages(forms.ModelForm):
    class Meta:
        model = ReferenceModel
        fields = ["caption", "image"]
