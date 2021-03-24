# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:02:20 2021

@author: Han Jae Woong
"""
from nltk.tag import pos_tag
import pandas as pd
data = pd.read_excel("./Trend_keywords.xlsx")


contents = []
for sentence in data['content']:
    contents.append(sentence)
    
words = []
for word in contents:
    a = word.split()
    for b in a:
        words.append(b)
        
def flat_list(array): 
    a=[]
    for i in array:
        if type(i) == type(list()):
            a+=(flat_list(i))       
        else:
            a.append(i)
    return a

# Counter
from collections import Counter
abstract_list = flat_list(words)
abstract = Counter(abstract_list)
abstract

# OrderDict
from collections import OrderedDict
def sort_by_key(t):
    return t[1]
for k, v in OrderedDict(sorted(abstract.items(), key=sort_by_key, reverse=True)).items():
    if len(k) == 3 and str(k).istitle() == True:
        print(k,v)
        

# Noun bi-gram
tagged_list = pos_tag(words)
word_li = []
for t in tagged_list:
    if (t[1] == 'NNS' or t[1] == 'NNPS'):
        word_li.append(t[0])
words=word_li              # 공백을 기준으로 문자열을 분리하여 리스트로 만듦
word_li = [] 
for i in range(len(words) - 1):      # 2-gram이므로 리스트의 마지막에서 요소 한 개 앞까지만 반복함
    aa = (words[i]+' '+words[i+1])
    word_li.append(aa)    # 현재 문자열과 그다음 문자열 출력
    