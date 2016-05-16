# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:42:23 2016

@author: zhcao
"""

"""
load dependencies
"""

import sklearn.linear_model as lm
import sklearn.feature_extraction as fe
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report,accuracy_score
import numpy as np
from sklearn.preprocessing import Imputer as im



def main():
    product=load_file('./amazon_baby.csv')
    X,y=preprocess(product)
#    print(np.shape(X),np.shape(y))
    # classifier, y_true,y_predict=classifier_model(X,y)
    # evaluation_model(y_true,y_predict)
#    print(y_true[0:50],y_predict[0:50])
    # print(classifier.coef_)

def load_file(file_dir):
    """
    read in the csv reviews data and drop the NaN data block
    """
    if isinstance(file_dir,str):

        return pd.read_csv(file_dir).dropna() #drop the NAN value for later processing

    else:
        raise NameError('Input file directory name should be a string!')

def preprocess(file):
    """
    build countvectorizer object, the vocabulary is the tokens list
    """

    """
    delete the rating==3 because it is too neutral
    """
    file=file[file.loc[:,'rating']!=3]
    # selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', \
    # 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']

    selected_words=[file['review'].iloc[89]]
    # print(np.shape(selected_words))
    # print(type(selected_words))
    # print(selected_words.head)
    text_cv=fe.text.CountVectorizer()
    # analyzer=text_cv.build_analyzer()
    # word_tokens=analyzer(file['review'].iloc[1])
    # print(np.shape(word_tokens))
    """
    build tfidf vectorizer object, add weighting to the domainant feature words
    """
    # text_cv=fe.text.TfidfVectorizer(vocabulary=selected_words)

    # review_sparse_matrix=text_cv.fit_transform(file['review'].values)
    review_sparse_matrix=text_cv.fit_transform(selected_words)

    count_matrix=review_sparse_matrix.toarray() #convert sample texts to sparse count matrix
    print(np.shape(count_matrix))
    print(count_matrix)
    # print(dict(zip(word_tokens,zip(*count_matrix))))

    most_used_word=selected_words[np.argmax(np.sum(count_matrix,axis=0))]

    least_used_word=selected_words[np.argmin(np.sum(count_matrix,axis=0))]

    print('Most used word:',most_used_word,'Least used word:',least_used_word)
    columns_count=pd.DataFrame(count_matrix,columns=selected_words)

#    print(columns_count.head)
#    file=pd.concat([raw_reviews,columns_count],axis=1,join_axes=[file.index])

    """
    sentiment classification: positive (1) and negtive (0), set the threshold based on the rating
    postive sentiment 4 or 5 rating, else are negtive
    """

    file['sentiment']=(file['rating']>=4)*1.0 # convert boolean value to 0 or 1


    data=columns_count.values

    target=file['sentiment'].values

    return data, target



def classifier_model(data, target):
    """
    using the logistic regression model as the binary class calssifier
    """

    data_train,data_test,target_train,target_test=cv.train_test_split(data,target, \
    test_size=0.2,random_state=66)

#    train_data[:,3:14]=im().fit_transform(train_data[:,3:14])
#
#    test_data[:,3:14]=im().fit_transform(test_data[:,3:14])

#    print(np.shape(data_train),np.shape(target_train))
#
#    print(np.shape(data_test),np.shape(target_test))

    sentiment_classifier_binary=lm.LogisticRegression(C=1.0,penalty='l2')


    sentiment_classifier_binary.fit(data_train,target_train)

    target_predicted=sentiment_classifier_binary.predict(data_test)

    return sentiment_classifier_binary, target_test,target_predicted,

################################################################################
"""
according the max review string length to determine which product has most reviews,
most popular product.

"""
#review_max_len=max((raw_reviews['review'].values),key=len)
#
#ind=raw_reviews[raw_reviews['review'].values==review_max_len].index
#
#most_reviewed_product=raw_reviews.loc[ind,'name']
#
#print('The popular purchased product is:',most_reviewed_product.values)

################################################################################


#print(sentiment_classifier_binary.coef_)


def evaluation_model(target_true, target_predicted):
    """
    using the classification metrics to measure the roc curve
    """

    print(classification_report(target_true,target_predicted))

    print(accuracy_score(target_true,target_predicted))
#    print ("The probability for the two classes:" )
#    test_predict_data=sentiment_classifier_binary.predict(test_data[:,3:14])
#
#    probability=sentiment_classifier_binary.predict_proba(test_data[:,3:14].astype(float))
#
#    fpr, tpr, thresholds=roc_curve(test_data[:,14],test_predict_data)



main()
