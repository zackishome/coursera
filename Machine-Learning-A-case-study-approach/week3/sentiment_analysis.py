# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:42:23 2016

@author: zhcao
"""

import sklearn.linear_model as lm
import sklearn.feature_extraction as fe
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import mean_squared_error 
import numpy as np

# read in the csv reviews data and drop the NaN data block

raw_reviews=pd.read_csv('./amazon_baby.csv').dropna()
#print(raw_reviews.head())
review=raw_reviews['review']
#print(raw_reviews['review'].head())
#print (type(['a','b','c']))
#print(type(review))

print(np.shape(review))
#build countvectorizer object

text_cv=fe.text.CountVectorizer(min_df=1)
#
#review_sparse_matrix=text_cv.fit_transform(review)

#selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', \
#'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']

selected_words=review.values

#print(type(selected_words))
#
print(np.shape(selected_words))

analyzer=text_cv.build_analyzer(selected_words)

print(text_cv.get_feature_names())


#print(raw_reviews.head())
#print(type(reviews_wordcount))



