from django.urls import path, re_path
from .views import (
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_create_view,
    blog_post_update_view,
    blog_post_delete_view,
)

urlpatterns = [
    path('', blog_post_list_view),
    re_path(r'^create?/$', blog_post_create_view, name='create'),
    path('<str:slug>', blog_post_detail_view, name='detail'),
    path('<str:slug>/edit/', blog_post_update_view, name='update'),
    path('<str:slug>/delete/', blog_post_delete_view, name='delete'),
]