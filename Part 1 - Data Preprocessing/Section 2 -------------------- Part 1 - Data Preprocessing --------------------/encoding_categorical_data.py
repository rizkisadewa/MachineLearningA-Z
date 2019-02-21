# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:49:27 2019

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

#Encoding Categorical Data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() # Make an object of LabelEncoder
X[:,0] = labelencoder_X.fit_transform(X[:,0]) # Assign variable X to Encoding the data from column number 0 using method fit_transform()
# Make a dummy encoding since the column contain 3 values
onehotencoder = OneHotEncoder(categorical_features = [0]) # Make an object of OneHotEncoder, set column number 0 as a dummy encoder
X = onehotencoder.fit_transform(X).toarray() # Make a dummy Encoding and make it to array

#Encoding Variable Y
labelencoder_Y = LabelEncoder() # Make an object of Label Encoder
Y = labelencoder_Y.fit_transform(Y) # Assign variable Y to Encoding the data from column number 2 using method fit_transform()
'''
If the column only contain 2 values, we do not have to make a dummy encoding due to the 
Machine will know it.
'''