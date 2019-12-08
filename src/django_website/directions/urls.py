from django.urls import path

from . import views

urlpatterns = [
    path('', views.directions_view, name='directions'),   
]