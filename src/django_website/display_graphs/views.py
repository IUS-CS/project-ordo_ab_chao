from django.shortcuts import render
from ebaysdk.finding import Connection as finding
import xmltodict
from json import loads, dumps
import pandas as pd


def display_the_graphs(request):
    keywords = request.POST.get('search')
    api = finding(appid='JohnHein-homepage-PRD-392e94856-07aba7fe', config_file=None, siteid='EBAY-US')
    api_request = {'keywords':keywords, 'itemFilter':[{'name':'SoldItemsOnly', 'value':True},]}
    response = api.execute('findCompletedItems', api_request)
    content = response.content
    xml_dict = xmltodict.parse(content)
    content_dict = to_dict(xml_dict)
    count = content_dict['findCompletedItemsResponse']['searchResult']['@count']
    context = {'response':content_dict}
    print('count:', count)
    extract_values(content_dict, count)
    return render(request, 'display_graphs/graphs.html', context)


def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))


def extract_values(temp_dict, count):
    df = pd.DataFrame(columns=['title'])
    
            