# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 09:52:53 2019

@author: rizky
"""

# Simple Linear Regression 

# Import the Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Salary_Data.csv')

# Make a matrix feature of the three independent variables
X = dataset.iloc[:,:-1].values
# Create the dependent variable vector
Y = dataset.iloc[:,1].values

# Splitting the dataset into Trainning set and Testing set
from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 1/3, random_state = 0)

'''
1/3 is to set 10 as a test set
'''

# Feature Scaling
"""
from sklearn.preprocessing import StandardScaler # import class from library
sc_X = StandardScaler() # an object from the class above
X_train = sc_X.fit_transform(X_train) # fit the object and transform it 
X_test = sc_X.transform(X_test) # we only transfer the object as it's already fitted in train set
""""
'''
for the dependent variable vector do not have to be scalled due to the the value represent
as category with 2 value "yes" or "no"
'''

# Fitting Simple Linear Regression to the Train Set 
from sklearn.linear_model import LinearRegression # import the library for fitting
regressor = LinearRegression() # make an object
regressor.fit(X_train, Y_train) # fit the train set 
'''
The above will make machine learn from train set and learn the coorelation use a Simple Linear Regression
'''

# Predict the Test set result
Y_pred = regressor.predict(X_test)

# Visualising the Trainning set results 
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Trainning Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Trainning set results 
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()