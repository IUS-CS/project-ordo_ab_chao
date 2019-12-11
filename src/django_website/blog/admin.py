from django.contrib import admin
from .models import BlogPost

# register BlogPost instance with django admin
admin.site.register(BlogPost)