from django.urls import path

from . import views

urlpatterns = [
    path('', views.about_website_view, name='about_website'),   
]