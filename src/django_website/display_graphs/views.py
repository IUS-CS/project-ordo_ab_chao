from django.shortcuts import render
from ebaysdk.finding import Connection as finding
import xmltodict
from json import loads, dumps
import pandas as pd
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse

content_df = pd.DataFrame()

def display_the_graphs(request):
    keywords = request.POST.get('search')
    api = finding(appid='JohnHein-homepage-PRD-392e94856-07aba7fe', config_file=None, siteid='EBAY-US')
    api_request = {'keywords':keywords, 'itemFilter':[{'name':'SoldItemsOnly', 'value':True},]}
    response = api.execute('findCompletedItems', api_request)
    content = response.content
    xml_dict = xmltodict.parse(content)
    content_dict = to_dict(xml_dict)
    count = content_dict['findCompletedItemsResponse']['searchResult']['@count']
    item_dict = content_dict['findCompletedItemsResponse']['searchResult']['item']
    print('count:', count)
    content_df = extract_values(item_dict)
    context = {'response':content_df.to_html(), 'content_df':content_df}
    return render(request, 'display_graphs/graphs.html', context)
'''
def get_time_graph(request):
    fig, ax = plt.subplots()
    ax.set_title('Scatter plot of prices over time')
    ax.set_xlabel('dates')
    ax.set_ylabel('sell prices')
    ax.scatter(content_df.endDate.values, content_df.endPrice.values, s=10, label='sell prices over time')
    canvas = FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    canvas.print_png(response)
    context = {'first_graph':response}
    return render(request, 'display_graphs/graphs.html', context)
'''
def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))

def extract_values(temp_dict):
    df = pd.DataFrame(columns=['itemId','title','endPrice','location','endTime'])
    a = []
    b = []
    c = []
    d = []
    f = []
    #print('\ntype of data:\n', type(temp_dict))
    length = len(temp_dict)
    print('\nlength:\n', length)
    for index in range(length):
        for key, value in temp_dict[index].items():
            print('temp_dict[index][key]:', key)
            if key == 'itemId':
                a.append(value)
            if key == 'title':
                b.append(value)
            if key == 'sellingStatus':
                c.append(temp_dict[index]['sellingStatus']['currentPrice']['#text'])
            if key == 'location':
                d.append(value)
            if key == 'listingInfo':
                f.append(temp_dict[index]['listingInfo']['endTime'])
    df = pd.DataFrame({'itemId':pd.Series(a),'title':pd.Series(b),'endPrice':pd.Series(c),'location':pd.Series(d),'endTime':pd.Series(f)})  
    #print('\ndf:\n', df)
    #print('\narray a:\n', a)
    #print('\narray b:\n', b)
    #print('\narray c:\n', c)
    #print('\narray d:\n', d)
    #print('\narray f:\n', f)
    df['endTime'] = pd.to_datetime(df['endTime'])
    df['endTime'],df['endDate'] = df['endTime'].apply(lambda x:x.time()),df['endTime'].apply(lambda x:x.date())
    return df


