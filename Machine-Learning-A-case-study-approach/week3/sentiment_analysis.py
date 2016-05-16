# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:42:23 2016

@author: zhcao
"""

"""
dependencies
"""

import sklearn.linear_model as lm
import sklearn.feature_extraction as fe
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import roc_curve
import numpy as np
from sklearn.preprocessing import Imputer as im
"""
read in the csv reviews data and drop the NaN data block
"""
raw_reviews=pd.read_csv('./amazon_baby.csv').dropna() #drop the NAN value for later processing
#print(raw_reviews.head())
review=raw_reviews['review'] #select the review text
#print(raw_reviews['review'].head())
#print (type(['a','b','c']))
#print(type(review))

"""
build countvectorizer object, the vocabulary is the tokens list
"""

selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', \
'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']

text_cv=fe.text.CountVectorizer(vocabulary=selected_words)

review_sparse_matrix=text_cv.fit_transform(review.values)

count_matrix=review_sparse_matrix.toarray() #convert sample texts to sparse count matrix

most_used_word=selected_words[np.argmax(np.sum(count_matrix,axis=0))]

least_used_word=selected_words[np.argmin(np.sum(count_matrix,axis=0))]


"""
according the max review string length to determine which product has most reviews,
most popular product.

"""
review_max_len=max((raw_reviews['review'].values),key=len)

ind=raw_reviews[raw_reviews['review'].values==review_max_len].index

most_reviewed_product=raw_reviews.loc[ind,'name']

print('The popular purchased product is:',most_reviewed_product.values)


"""
sentiment classification: positive (1) and negtive (0), set the threshold based on the rating
postive sentiment 4 or 5 rating, else are negtive
"""

raw_reviews['count']= np.sum(count_matrix,axis=1)

raw_reviews['count']=count_matrix.tolist

columns_count=pd.DataFrame(count_matrix,columns=selected_words)
# raw_reviews=pd.

raw_reviews=pd.concat([raw_reviews,columns_count],axis=1,join_axes=[raw_reviews.index])

print(raw_reviews.head())

raw_reviews['sentiment']=(raw_reviews['rating']>=4)*1.0 # convert boolean value to 0 or 1

print(raw_reviews.head())
#review_count_matrix=fe.text.TfidfVectorizer.fit_transform(review.values[0]).toarray()

train_data,test_data=cv.train_test_split(raw_reviews, test_size=0.2,random_state=66)

train_data[:,3:14]=im().fit_transform(train_data[:,3:14])
#
test_data[:,3:14]=im().fit_transform(test_data[:,3:14])



sentiment_classifier_binary=lm.LogisticRegression(C=1.0,penalty='l2')


sentiment_classifier_binary.fit(train_data[:,3:14],train_data[:,14])


#print(sentiment_classifier_binary.coef_)




"""
using the classification metrics to measure the roc curve
"""
test_predict_data=sentiment_classifier_binary.predict(test_data[:,3:14])

probability=sentiment_classifier_binary.predict_proba(test_data[:,3:14].astype(float))



fpr, tpr, thresholds=roc_curve(test_data[:,14],test_predict_data)




"""
debuging region history

#selected_words=review.values

#print(selected_words[0])
#
#print(np.shape(selected_words))
#x="help me out."

#analyzer=text_cv.build_analyzer()

#print(np.size(text_cv.get_feature_names()))
#analyzer(selected_words[0])

#a=review_sparse_matrix.toarray()
#print(a[0:5,0:3])

#print(text_cv.get_feature_names())
#print(raw_reviews.head())
#print(type(reviews_wordcount))

"""
