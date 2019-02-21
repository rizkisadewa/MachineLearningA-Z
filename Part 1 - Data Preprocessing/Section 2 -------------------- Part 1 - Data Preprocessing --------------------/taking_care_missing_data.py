# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:48:41 2019

@author: rizky
"""

# Data Processing 

# Import the Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Data.csv')

# Make a matrix feature of the three independent variables
X = dataset.iloc[:,:-1].values
# Create the dependent variable vector
Y = dataset.iloc[:,3].values

# Splitting the dataset into Trainning set and Testing set
from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

'''
the remark will be updated soon
'''

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) #setting imputer
imputer = imputer.fit(X[:, 1:3]) # fit the imputer into independent variable X
X[:, 1:3] = imputer.transform(X[:, 1:3]) # transform a value NaN as per setting above
'''
Setting Imputer
missing_values is the parameter to look for the missing value in column
strategy is the parameter to set a value from the method, a few method that we can use
1. mean = then replacing missing values using the mean along the axis, is the same in average
2. median = then replacing missing values using the median along the axis
3. most_frequent = then replacing missing values using the most frequent along the axis

axis
if axis = 0 then input along columns
if axis = 1 then input along lines
'''