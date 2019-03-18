# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:04:08 2019

@author: rizky
"""

# Multiple Linear Regression 

# Data Processing 

# Import the Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('50_Startups.csv')

# Make a matrix feature of the three independent variables
X = dataset.iloc[:,:-1].values
# Create the dependent variable vector
Y = dataset.iloc[:,4].values

#Encoding Categorical Data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() # Make an object of LabelEncoder
X[:,3] = labelencoder_X.fit_transform(X[:,3]) # Assign variable X to Encoding the data from column number 0 using method fit_transform()
# Make a dummy encoding since the column contain 3 values
onehotencoder = OneHotEncoder(categorical_features = [3]) # Make an object of OneHotEncoder, set column number 0 as a dummy encoder
X = onehotencoder.fit_transform(X).toarray() # Make a dummy Encoding and make it to array

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

'''
If the column only contain 2 values, we do not have to make a dummy encoding due to the 
Machine will know it.
'''

# Splitting the dataset into Trainning set and Testing set
from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

'''
the remark will be updated soon
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

# Fitting Multiple Linear Regression 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train) # we fit the independent variable and dependent variable into regressor 

# Predicting the Test set result 
Y_pred = regressor.predict(X_test)

# Building The Optimal Model using Backward Elimination 
import statsmodels.formula.api as sm
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
         
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)


