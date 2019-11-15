from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_the_graphs, name='graphs'),   
]