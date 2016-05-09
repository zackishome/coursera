
import sklearn.linear_model as lm
import sklearn.feature_extraction as fe
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import mean_squared_error 
import numpy as np

raw_reviews=pd.read_csv('./amazon_baby.csv')
#print(raw_reviews.head())
review=raw_reviews['review'].to_string()
#print(raw_reviews['review'].head())
#print (type(['a','b','c']))
#print(type(review))

reviews_wordcount=fe.text.CountVectorizer(min_df=1).fit_transform(review)

print(type(reviews_wordcount))



