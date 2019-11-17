from django.test import TransactionTestCase
from django.test import TestCase
#from django.urls import reverse
from home_page.models import Search
from ebaysdk.finding import Connection as finding

class PageTest(TransactionTestCase):
    
    def test_home_page_status_code_1(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_home_page_status_code_2(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
        
    def test_graphs_page_status_code(self):
        response = self.client.get('/graphs/')
        self.assertEquals(response.status_code, 200)
        
    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEquals(response.status_code, 200)
        
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)
        
    def test_blog_page_status_code(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)
        
class SearchModelTest(TestCase):
    
    def test_keywords_respresentation(self):
        keywords1 = Search(search="1986 Fleer Jordan")
        keywords2 = Search(search=1986)
        self.assertEquals(str(keywords1), keywords1.search)
        self.assertNotEquals(keywords2, keywords2.search)
        
class TestEbayAPI(TestCase):
    
    def test_ebay_request_status_code(self):
        api = finding(appid='JohnHein-homepage-PRD-392e94856-07aba7fe', config_file=None, siteid='EBAY-US')
        keywords = Search(search="1986 Fleer Jordan PSA 10")
        api_request = {'keywords':keywords, 'itemFilter':[{'name':'SoldItemsOnly', 'value':True},]}
        response = api.execute('findCompletedItems', api_request)
        self.assertEqual(response.status_code, 200)