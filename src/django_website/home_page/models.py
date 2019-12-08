from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=300)
    
    def __str__(self):
        return self.search