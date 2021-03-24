# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:07:41 2021

@author: Han Jae Woong
"""

import requests
import time
import pandas as pd

url_post = 'http://www.patentsview.org/api/patents/query'
post_len = 10000

#Don't touch ('Only patent_date ex)yyyy-mm-dd')
q1 = '?q={"_and":[ {"_gte":{"patent_date":"2010-01-01"}},{"_or":[{"_text_all":{"patent_title":'
q2 = '}},{"_text_all":{"patent_abstract":'
q3 = '}}]}]}'

q = '?q={"_and":[ {"_gte":{"patent_date":"2010-01-01"}},{"_or":[{"_text_all":{"patent_title":search_t}},{"_text_all":{"patent_abstract":search_t}}]}]}'


# 2-1) patent keyword
searchText_f = ['decentralized']
searchText_b = ['data','block','system','network','device','transaction','information','method','plurality','transactions', 'ledger', 'value', 'hash', 'request','contract','computer','blocks','node','service', 'identity']
searchText_T=[]
for f in searchText_f:
    for b in searchText_b:
        searchText_T.append(f+" "+b)
# search_Text_a = ['self-sovereign identity','distributed ledger technology','smart contract', 'directed acyclic graph']
# for x in search_Text_a:
#     searchText_T.append(x)
print(searchText_T)
print(len(searchText_T))

# post total page list
total_patent = []

# post data
for t,search_t in enumerate(searchText_T):
    print("search num: ",t)
    print("search text: ", search_t)
    st = time.time()
    pt_dict_list = []
    # post first page
    try:
        q=q1+'"'+searchText_T[t]+'"'+q2+'"'+searchText_T[t]+'"'+q3
        f = '&f=["patent_number","patent_title","patent_date","ipc_section","ipc_class","ipc_subclass","patent_type","patent_abstract"]'
        o = '&o={"page":1,"per_page":10000}'
        o1 = '&o={"page":'
        o3 = ',"per_page":10000}'
        o = o1+str(t+1)+o3
        #print(q)
        t_data = q+f+o
        #print(t_data)
        t_post = requests.post(url_post+t_data).json()
        #print(t_post)
        print("total_patent_num :",t_post['total_patent_count'])
        pt_dict_list.extend(t_post['patents'])
        post_page = int(t_post['total_patent_count']/post_len)+2
        print("post page: ",post_page)
        
    except:
        print("=== Try error1 ===")
    
    # post total page
    if post_page >2:                   
        for n in range(2,post_page):
            
            print("page number :",n,"/",post_page)
            try:
                #data = post_data(n,post_len,patent_date,search_t)
                js_data_post = requests.post(url_post+t_data).json()
                pt_dict_list.extend(js_data_post['patents'])
            
            except:
                print("=== Try error2 ===")
            
            
    et = time.time()
    print("exe_time :",et-st)
    time.sleep(1)   
    total_patent.extend(pt_dict_list)
    

# filter util patent (not design etc..)
util_patent = []
for pat in total_patent:

    if pat['patent_type'] == 'utility':
          util_patent.append(pat)

print(util_patent[0])


# cpcs ->list
st = time.time()
for d in util_patent:
    cpc_set = ''
    for c in d['cpcs']:
        try:
            cpc = c['cpc_subgroup_id'].split('/')[0]
            cpc_set = cpc_set + ',' + cpc
        except:
            cpc_set = cpc_set + 'None'
    d['cpc_set'] = cpc_set

et = time.time()
print("exe_time :",et-st)

print(util_patent[0])

# dict to dataframes
df = pd.DataFrame.from_dict(util_patent).drop(['cpcs'],axis=1)

print(df.iloc[0])
print('='*50)
print(df['cpc_set'][0])


# drop duplicates
df.drop_duplicates(['patent_number'], inplace=True)

# save to csv file
cpc_set_cpc = []

for cpc in df['cpc_set']:
    split_cpc = cpc.split(',')
    cpc = ' '.join(split_cpc).split()
    each_set = []
    for each in cpc:
        each_set.append(each)
    cpc_set_cpc.append(each_set)
    