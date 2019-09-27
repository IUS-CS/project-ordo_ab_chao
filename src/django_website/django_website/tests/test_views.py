from django.test import TestCase
#from django.urls import reverse
from django_website.views import homepage

class homepageTestCase(TestCase):
    
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        