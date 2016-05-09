# Author: zhihui cao
# Email: zhcaoulaval@gmail.com
# This is the assignment for multi features regression estimation for "Machine Learning: A Case Study Approach" from
# university washington in coursera.org

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model as lm
from sklearn import cross_validation as cv
from sklearn.metrics import mean_squared_error 
import numpy as np

########load dataset with pandas read csv
data_in_csv=pd.read_csv('./home_data.csv')

#print(data_in_csv.head())

# print the size of the dataset,number of houses and its features
#print(data_in_csv.shape)

########select features and target from the dataset
# features used to estimate the price 
features_flag=1

if features_flag==1:
	features=['sqft_living']
	#features=['bedrooms','bathrooms','sqft_living','sqft_lot','floors','zipcode']
else:
	features=['bedrooms','bathrooms','sqft_living','sqft_lot','floors','zipcode',
	'condition', 
	'grade',
	'waterfront',
	'view',
	'sqft_above',
	'sqft_basement',
	'yr_built',    
	'yr_renovated',
	'lat','long',
	'sqft_living15',
	'sqft_lot15'
	]

data_features=data_in_csv[features]
data_price=data_in_csv['price']
#print(type(data_features))
print(type(data_price))
print(type(data_features))
data_price_zipcode=data_in_csv[(data_in_csv['zipcode']==98039)]['price']
print('avarage price of zipcode 98039 (seatle area) \n',np.mean(data_price_zipcode))

data_price_sqftliving=data_in_csv[((data_in_csv['sqft_living']>2000)&(data_in_csv['sqft_living']<4000))]
print('the portion of house between 2000 and 4000 sqft_living \n',data_price_sqftliving.shape[0]/data_in_csv.shape[0])

######## data set split
data_features_train ,data_features_test,data_price_train, data_price_test=cv.train_test_split(data_features,data_price,test_size=0.2,random_state=0)
#data_price_train_reshape=data_price_train.values.reshape(len(data_price_train.values),1)

#data_price_test_reshape=data_price_test.values.reshape(len(data_price_test.values),1)
# print(data_price_train_reshape.shape)

##### multip feature linear regression
lr=lm.LinearRegression(fit_intercept=True,copy_X=True)
lr_model=lr.fit(data_features_train.values,data_price_train.values)
# scores=lr_model.score(data_features_test,data_price_test)
#print(lr.coef_)
# print(scores)
print('Coefficients:\n',list(zip(features,lr_model.coef_)))
#zip(features,lr_model.coef_)
print('Intercept:\n',lr_model.intercept_)
#print(type(lr_model.coef_))

# calculate the rmse of the model
predict_price=lr_model.predict(data_features_test)

print(predict_price.shape)

print('metric \n' ,np.sqrt(mean_squared_error(data_price_test.values,predict_price,multioutput='raw_values')))
#print(type(data_price_test))
#print((predict_price-data_price_test).values)
print('Residual sum of squares: %.3f' %np.sqrt(np.mean(((predict_price-data_price_test)) ** 2)))

# print('variance score: %.2f' %lr_model.score(data_features_test.values,data_price_test.values))

# plot output
# plt.scatter(data_features_test,data_price_test,color='black')
# plt.plot(data_features_test,predict_price,color='red')
# plt.xticks(())
# plt.yticks(())

# plt.show()
