from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) # Example: "hello world" -> hello-world
    content = models.TextField(null=True, blank=True)
    
