from django.shortcuts import render, get_object_or_404
import requests
from requests.compat import quote_plus
from . import models

keywords = ''
BASE_EBAY_URL = 'https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems&SERVICE-NAME=FindingServices&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=JohnHein-homepage-PRD-392e94856-07aba7fe&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords='+keywords+'&itemFilter(0).name=SoldItemsOnly&itemFilter(0).value=true&paginationInput.entriesPerPage=3'
# Create your views here.
def homepage(request):
    return render(request, 'home_page/homepage.html')

def display_graphs(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    print('key search words formatted:', quote_plus(search))
    final_url = BASE_EBAY_URL.format(quote_plus(search))
    print('final_url:', final_url)
    print('search words are:', search)
    response = requests.get(final_url)
    print('JSON response:', response)

    return render(request, 'my_app/new_search.html', {})