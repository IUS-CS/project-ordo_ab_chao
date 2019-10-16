from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'), 
    path('', views.display_graphs, name='graphs'),   
]