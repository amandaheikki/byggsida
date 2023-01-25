from django.urls import path
from . import views
from .views import startpage_items, startpage_update, startpage_contentupd1, startpage_contentupd2, startpage_contentupd3, startpage_content, aboutpage_items, aboutpage_update, aboutpage_updateBox1, update_servicesheading, services_items, update_servicescontent1, update_servicescontent2, update_estimateheading, estimate_items, contact_items, update_contactheading, displayImages, add_image, delete_image

urlpatterns = [
    path('/', startpage_items, name="index"),
    path('/', startpage_content, name="index"),
    path('<id>/update', startpage_update, name="update"),
    path('<id>/updatecontent', startpage_contentupd1, name="updatecontent"),
    path('<id>/updatecontent2', startpage_contentupd2, name="updatecontent2"),
    path('<id>/updatecontent3', startpage_contentupd3, name="updatecontent3"),
    path('/about', aboutpage_items, name="about" ),
    path('<id>/update_about1', aboutpage_update, name="update_about1"),
    path('<id>/update_about2', aboutpage_updateBox1, name="update_about2"),
    path('/services', services_items, name="services"),
    path('<id>/update_serviceheading', update_servicesheading, name="update_serviceheading"),
    path('<id>/update_service1', update_servicescontent1, name="update_service1"),
    path('<id>/update_service2', update_servicescontent2, name="update_service2"),
    path('/estimate', estimate_items, name="estimate"),
    path('<id>/update_estimateheading', update_estimateheading, name="update_estimateheading"),
    path('/contact', contact_items, name="contact"),
    path('<id>/update_contactheading', update_contactheading, name="update_contactheading"),
    path('/references', displayImages, name="references"),
    path('/upload_images', add_image, name="upload_images"),
    path('<int:pk>', delete_image, name="delete_image"),
    path('/about', views.about, name='about'),
    path('/references', views.references, name='references'),
    path('/contact', views.contact, name='contact'),
    path('/services', views.services, name='services'),
    path('/estimate', views.estimate, name='estimate'),
    
]