from django.db import models

# create instance of object with keyword search on home page
class Search(models.Model):
    search = models.CharField(max_length=300)
    
    def __str__(self):
        return self.search