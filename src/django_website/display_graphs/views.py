from django.shortcuts import render
from ebaysdk.finding import Connection as finding
import xmltodict
from json import loads, dumps
import pandas as pd
import numpy as np
import datetime

content_df = pd.DataFrame()

def display_the_graphs(request):
    keywords = request.POST.get('search')
    api = finding(appid='JohnHein-homepage-PRD-392e94856-07aba7fe', config_file=None, siteid='EBAY-US')
    api_request = {'keywords':keywords, 'itemFilter':[{'name':'SoldItemsOnly', 'value':True},],'outputSelector':['SellerInfo']}
    response = api.execute('findCompletedItems', api_request)
    content = response.content
    xml_dict = xmltodict.parse(content)
    content_dict = to_dict(xml_dict)
    count = content_dict['findCompletedItemsResponse']['searchResult']['@count']
    item_dict = content_dict['findCompletedItemsResponse']['searchResult']['item']
    print('count:', count)
    print('\nitem_dict:\n', item_dict)
    content_df = extract_values(item_dict)
    y_values = content_df['endPrice'].tolist()
    y_values = [float(i) for i in y_values]
    x_values_b = content_df['endTime'].tolist()
    x_values = convert_datetime(x_values_b)
    #print('\nx_values: ', x_values,'\n')
    #print('\ny_values: ', y_values,'\n')
    #print('\nx_values count:', len(x_values),'\n')
    #print('\ny_values count:', len(y_values),'\n')
    #print('\nx_values type:', type(x_values[-1]),'\n')
    #print('\ny_values type:', type(y_values[-1]),'\n')
    chart1_data = [list(i) for i in zip(x_values, y_values)]
    df2 = out_of_sample(content_df)
    df3 = neural_network(content_df)
    #print('chart1 data:', chart1_data)
    context = {
        'response': content_df.to_html(),
        'chart1': chart1_data,
        'oos_df': df2.to_html(),
        'nn_df': df3.to_html()
    }
    return render(request, 'display_graphs/graphs.html', context)

def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))

def extract_values(temp_dict):
    df = pd.DataFrame(columns=['itemId','title','listingType','endPrice','shippingServiceCost','bidCount','watchCount','returnsAccepted','location','endTime','startTime','handlingTime','sellerUserName','feedbackScore','positiveFeedbackPercent','topRatedSeller'])
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    #print('\ntype of data:\n', type(temp_dict))
    length = len(temp_dict)
    #print('\nlength:\n', length)
    for index in range(length):
        for key, value in temp_dict[index].items():
            #print('temp_dict[index][key]:', key)
            if key == 'itemId':
                a.append(value)
            if key == 'title':
                b.append(value)
            if key == 'sellingStatus':
                c.append(temp_dict[index]['sellingStatus']['convertedCurrentPrice']['#text'])
                try:
                    d.append(temp_dict[index]['sellingStatus']['bidCount'])
                except KeyError:
                    d.append(np.nan)
            if key == 'shippingInfo':
                e.append(temp_dict[index]['shippingInfo']['handlingTime'])
                try:
                    m.append(temp_dict[index]['shippingInfo']['shippingServiceCost']['#text'])
                except KeyError:
                    m.append(np.nan)
            if key == 'sellerInfo':
                f.append(temp_dict[index]['sellerInfo']['sellerUserName'])
                g.append(temp_dict[index]['sellerInfo']['feedbackScore'])
                h.append(temp_dict[index]['sellerInfo']['positiveFeedbackPercent'])
                n.append(temp_dict[index]['sellerInfo']['topRatedSeller'])
            if key == 'location':
                i.append(value)
            if key == 'listingInfo':
                j.append(temp_dict[index]['listingInfo']['endTime'])
                l.append(temp_dict[index]['listingInfo']['startTime'])
                p.append(temp_dict[index]['listingInfo']['listingType'])
                try:
                    k.append(temp_dict[index]['listingInfo']['watchCount'])
                except KeyError:
                    k.append(np.nan)
            if key == 'returnsAccepted':
                o.append(value)

    df = pd.DataFrame({'itemId':pd.Series(a),'title':pd.Series(b),'listingType':pd.Series(p),'endPrice':pd.Series(c),'shippingServiceCost':pd.Series(m),
                       'bidCount':pd.Series(d),'watchCount':pd.Series(k),'returnsAccepted':pd.Series(o),
                       'location':pd.Series(i),'endTime':pd.Series(j),'startTime':pd.Series(l),'handlingTime':pd.Series(e),
                       'sellerUserName':pd.Series(f),'feedbackScore':pd.Series(g),'positiveFeedbackPercent':pd.Series(h),
                       'topRatedSeler':pd.Series(n)})  
    #print('\ndf:\n', df)
    #print('\narray a:\n', a)
    #print('\narray b:\n', b)
    #print('\narray c:\n', c)
    #print('\narray d:\n', d)
    #print('\narray f:\n', f)
    df['endTime'] = pd.to_datetime(df['endTime']) # datetime ISO 8601 format ---> YYYY-MM-DD HH:MM:SS +HH:MM (NOTE: '+HH:MM' is UTC offset)
    df['endTimeOfDay'],df['endDate'] = df['endTime'].apply(lambda x:x.time()),df['endTime'].apply(lambda x:x.date())
    return df

def convert_datetime(arr):
    arr2 = []
    for i in arr:
        dateobj = str(i)
        dateobj = dateobj[:19]
        arr2.append(int(datetime.datetime.strptime(dateobj, "%Y-%m-%d %H:%M:%S").timestamp())*1000)
        #print('convert_datetime ',arr2[-1])
        #print('dateobj:', dateobj)
    return arr2

def out_of_sample(c_df):
    df = c_df.copy()
    df['endPrice'] = df['endPrice'].astype(float)
    pivot_df = df.pivot_table(index='endDate', columns='listingType', values='endPrice')
    pivot_df = pivot_df.interpolate(method='linear', axis=0).ffill().bfill()
    print('\npivot_df:\n', pivot_df)
    delta_values = [7,14,21,28]
    delta_dict = {}
    for offset in delta_values:
        delta_dict['delta_{}'.format(offset)] = pivot_df/pivot_df.shift(offset) - 1.0
    print('delta_7 \'date\' check for null dates:', delta_dict['delta_7'].index.isnull().sum())
    print('delta_14 \'date\' check for null dates:', delta_dict['delta_14'].index.isnull().sum())
    print('delta_21 \'date\' check for null dates:', delta_dict['delta_21'].index.isnull().sum())
    print('delta_28 \'date\' check for null dates:', delta_dict['delta_28'].index.isnull().sum())
    melted_dfs = []
    for key, delta_df in delta_dict.items():
        melted_dfs.append(delta_df.reset_index().melt(id_vars=['endDate'], value_name=key))
    for i in melted_dfs:
        print(i,'melted_dfs:\n', i.tail())
    target_variable = pd.merge(melted_dfs[0], melted_dfs[1], on=['endDate','listingType'])
    target_variable = pd.merge(target_variable, melted_dfs[2], on=['endDate','listingType'])
    target_variable = pd.merge(target_variable, melted_dfs[3], on=['endDate', 'listingType'])
    print('\ntarget_variable:\n', target_variable)
    return target_variable

def neural_network(n_df):
    df = n_df.copy()
    df['itemId'] = df['itemId'].astype(int)
    df['listingType'] = pd.get_dummies(df['listingType'])
    df['endPrice'] = df['endPrice'].astype(float)
    df['shippingServiceCost'] = df['shippingServiceCost'].astype(float)
    df['bidCount'] = df['bidCount'].astype(int)
    df['watchCount'] = df['watchCount'].astype(int)
    df['returnsAccepted'] = pd.get_dummies(df['returnsAccepted'])
    df['handlingTime'] = df['handlingTime'].astype(int)
    df['sellerUserName'] = pd.get_dummies(df['sellerUserName'])
    df['feedbackScore'] = df['feedbackScore'].astype(int)
    df['positiveFeedbackPercent'] = df['positiveFeedbackPercent'].astype(float)
    df['topRatedSeller'] = pd.get_dummies(df['topRatedSeller'])
    df['endDate'] = pd.get_dummies(df['endDate'])
    features = df.drop(['title','location','endTime','startTime','endTimeOfDay'])
    return df
