from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from .models import StartModel, EstimateModel, ContactModel, AboutModel, ServiceModel, ReferenceModel
from .form import updateStartPage, updateStartPageContent1, updateStartPageContent2, updateStartPageContent3, updateAboutPage, updateAboutContent1, updateAboutContent2, updateServiceHeading, updateServiceContent1, updateServiceContent2, updateEstimateHeading, addImages
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib import messages
from django.views.generic import CreateView, ListView

# Create your views here.

# All updates for index/startpage
def startpage_items(request):
    obj=StartModel.objects.all()
    return render(request, "index.html", {"obj":obj})


@login_required
def startpage_update(request, id):
    obj=get_object_or_404(StartModel, id=id)
    if request.method == "POST":
        form=updateStartPage(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        start_instance = StartModel.objects.get(id=1)   
        form=updateStartPage(instance=start_instance)
    return render(request, "update.html",{"form":form})    


def startpage_content(request):
    obj=StartModel.objects.all()
    return render(request, "index.html", {"obj":obj})

@login_required
def startpage_contentupd1(request, id):
    
    obj=get_object_or_404(StartModel, id=id)
    if request.method == "POST":
        form=updateStartPageContent1(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
       start_instance = StartModel.objects.get(id=1)   
       form=updateStartPageContent1(instance=start_instance)

    return render(request, "updatecontent.html",{"form":form})  

@login_required
def startpage_contentupd2(request, id):
    obj=get_object_or_404(StartModel, id=id)
    if request.method == "POST":
        form=updateStartPageContent2(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        start_instance = StartModel.objects.get(id=1)  
        form=updateStartPageContent2(instance=start_instance)
    return render(request, "updatecontent2.html",{"form":form})  

@login_required
def startpage_contentupd3(request, id):
    obj=get_object_or_404(StartModel, id=id)
    if request.method == "POST":
        form=updateStartPageContent3(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        start_instance = StartModel.objects.get(id=1)  
        form=updateStartPageContent3(instance=start_instance)
    return render(request, "updatecontent3.html",{"form":form}) 



# All updates for about us page

def aboutpage_items(request):
    obj=AboutModel.objects.all()
    return render(request, "about.html", {"obj":obj})

@login_required
def aboutpage_update(request, id):
    obj=get_object_or_404(AboutModel, id=id)
    if request.method == "POST":
        form=updateAboutPage(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
    else:
        start_instance = AboutModel.objects.get(id=1)  
        form=updateAboutPage(instance=start_instance)
    return render(request, "update_about1.html",{"form":form})    

@login_required
def aboutpage_updateBox1(request, id):
    obj=get_object_or_404(AboutModel, id=id)
    if request.method == "POST":
        form=updateAboutContent1(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
    else:
        start_instance = AboutModel.objects.get(id=1) 
        form=updateAboutContent1(instance=start_instance)
    return render(request, "update_about2.html",{"form":form})   

@login_required
def aboutpage_updateBox2(request, id):
    obj=get_object_or_404(AboutModel, id=id)
    if request.method == "POST":
        form=updateAboutContent2(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
    else:
        start_instance = AboutModel.objects.get(id=1) 
        form=updateAboutContent2(instance=start_instance)
    return render(request, "update_about3.html",{"form":form})  

# SERVICE

def services_items(request):
    obj=ServiceModel.objects.all()
    return render(request, "services.html", {"obj":obj})

@login_required
def update_servicesheading(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateServiceHeading(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/services")
    else:
        start_instance = ServiceModel.objects.get(id=1) 
        form=updateServiceHeading(instance=start_instance)
    return render(request, "update_serviceheading.html",{"form":form})  

@login_required
def update_servicescontent1(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateServiceContent1(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/services")
    else:
        start_instance = ServiceModel.objects.get(id=1) 
        form=updateServiceContent1(instance=start_instance)
    return render(request, "update_service1.html",{"form":form})  

@login_required
def update_servicescontent2(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateServiceContent2 (request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/services")
    else:
        start_instance = ServiceModel.objects.get(id=1) 
        form=updateServiceContent2(instance=start_instance)
    return render(request, "update_service2.html",{"form":form})  



#ESTIMATE
def estimate_items(request):
    obj=EstimateModel.objects.all()
    return render(request, "estimate.html", {"obj":obj})

@login_required
def update_estimateheading(request, id):
    obj=get_object_or_404(ServiceModel, id=id)
    if request.method == "POST":
        form=updateEstimateHeading(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/estimate")
    else:
        start_instance = EstimateModel.objects.get(id=1) 
        form=updateEstimateHeading(instance=start_instance)
    return render(request, "update_estimateheading.html",{"form":form})  

#CONTACT
def contact_items(request):
    obj=ContactModel.objects.all()
    return render(request, "contact.html", {"obj":obj})

@login_required
def update_contactheading(request, id):
    obj=get_object_or_404(ContactModel, id=id)
    if request.method == "POST":
        form=updateContactHeading(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/contact")
    else:
        start_instance = ContactModel.objects.get(id=1) 
        form=updateContactHeading(instance=start_instance)
    return render(request, "update_contactheading.html",{"form":form})  


#REFERENCES
@login_required
def add_image(request):
    if request.method == "POST":
        form = addImages(data=request.POST, files=request.FILES)
          
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/references")
    else:
        form = addImages()

    return render(request, "upload_images.html", {"form": form})

def displayImages(request):
    if request.method == "GET":
        img = ReferenceModel.objects.all()
        return render(request, "references.html", {"ref_img":img})
@login_required
def delete_image(request, pk):
    if request.method == "POST":
        img = ReferenceModel.objects.get(pk=pk)
        img.delete()
        return HttpResponseRedirect("/references")


def about(request):
    return render(request, 'about.html', {})

def references(request):
    return render(request, 'references.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def services(request):
    return render(request, 'services.html', {})    

def estimate(request):
    return render(request, 'estimate.html', {})    
