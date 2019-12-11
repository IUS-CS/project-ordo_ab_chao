from django.urls import path

from . import views

# render the 'about us' endpoint
urlpatterns = [
    path('', views.about_us, name='about'),     
]
