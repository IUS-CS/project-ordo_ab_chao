from django.shortcuts import render
from ebaysdk.finding import Connection as finding


# Create your views here.
def display_the_graphs(request):
    keywords = request.POST.get('search')
    api = finding(appid='JohnHein-homepage-PRD-392e94856-07aba7fe', config_file=None, siteid='EBAY-US')
    api_request = {'keywords':keywords}
    response = api.execute('findItemsByKeywords', api_request)
    content = response.content
    context = {'response':content}
    return render(request, 'display_graphs/graphs.html', context)