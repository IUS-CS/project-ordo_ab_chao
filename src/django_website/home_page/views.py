from django.shortcuts import render

keywords = ''
BASE_EBAY_URL = 'https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems&SERVICE-NAME=FindingServices&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=JohnHein-homepage-PRD-392e94856-07aba7fe&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords='+keywords+'&itemFilter(0).name=SoldItemsOnly&itemFilter(0).value=true&paginationInput.entriesPerPage=3'
# Create your views here.
def homepage(request):
    return render(request, 'home_page/homepage.html')
