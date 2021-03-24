# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:17:26 2021

@author: Han Jae Woong
"""

import pandas as pd
df = pd.read_csv("./core keywords set.csv")

cpc_set = []
for document in df.cpc_set:
    document = document.split(',')
    each_document = []
    for a in document:
        each_document.append(a)
    cpc_set.append(each_document)
    
documents = []
for document in cpc_set:
    s = " ".join(document)
    documents.append(s)
    
    
from sklearn.feature_extraction.text import TfidfVectorizer
text = documents
tfidf_vectorizer = TfidfVectorizer() # TF-IDF 객체선언

tfidf_vectorizer.fit(text) # 단어를 학습시킴 
tfidf_vectorizer.vocabulary_ # 단어사전을 출력 
sorted(tfidf_vectorizer.vocabulary_.items()) # 단어사전 정렬

# co-occurrence
import numpy as np
import nltk
from nltk import bigrams
import itertools
 
def generate_co_occurrence_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_index = {word: i for i, word in enumerate(vocab)}
 
    bi_grams = list(bigrams(corpus))
 
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))

    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))
 
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_index[current]
        pos_previous = vocab_index[previous]
        co_occurrence_matrix[pos_current][pos_previous] = count
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)
 
    return co_occurrence_matrix, vocab_index
 
text_data = cpc_set

data = list(itertools.chain.from_iterable(text_data))
matrix, vocab_index = generate_co_occurrence_matrix(data)
 
    
data_matrix = pd.DataFrame(matrix, index=vocab_index, columns=vocab_index)

print(data_matrix)

# Dataframe & Save to csv file
data = pd.DataFrame(data_matrix)
data.to_csv("co-occurrence core keyword.csv",encoding='utf8')


