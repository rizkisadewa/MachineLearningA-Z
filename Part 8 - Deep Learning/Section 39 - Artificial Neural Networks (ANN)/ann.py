# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:38:12 2019

@author: rizky
"""

# Artificial Neural Network
# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Data Processing 
# Import the Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Churn_modelling.csv')

# Make a matrix feature of the three independent variables
X = dataset.iloc[:, 3:13].values # we can see only in console by type X and enter it.
# Create the dependent variable vector
Y = dataset.iloc[:, 13].values

#Encoding Categorical Data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder() # Make an object of LabelEncoder
X[:,1] = labelencoder_X_1.fit_transform(X[:,1]) 
labelencoder_X_2 = LabelEncoder() # Make an object of LabelEncoder
X[:,2] = labelencoder_X_2.fit_transform(X[:,2]) 
# Make a dummy encoding since the column contain 3 values
onehotencoder = OneHotEncoder(categorical_features = [1]) # Make an object of OneHotEncoder, set column number 0 as a dummy encoder
X = onehotencoder.fit_transform(X).toarray() # Make a dummy Encoding and make it to array
X = X[:, 1:]


# Splitting the dataset into Trainning set and Testing set
from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler # import class from library
sc_X = StandardScaler() # an object from the class above
X_train = sc_X.fit_transform(X_train) # fit the object and transform it 
X_test = sc_X.transform(X_test) # we only transfer the object as it's already fitted in train set

'''
for the dependent variable vector do not have to be scalled due to the the value represent
as category with 2 value "yes" or "no"
'''


# Importing the keras libraries and packages 
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the Ann
classifier = Sequential()

# Adding the input layer and the first hidden
classifier.add(Dense(output_dim = 6, init='uniform', activation='relu', input_dim = 11))

# Adding the second hidden layer 
classifier.add(Dense(output_dim = 6, init='uniform', activation='relu'))

# Adding the output layer 
classifier.add(Dense(output_dim = 1, init='uniform', activation='sigmoid'))

# Compiling the ANN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
