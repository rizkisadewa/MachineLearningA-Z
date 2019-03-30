# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:20:32 2019

@author: rizky
"""

# Regression Template

# Import the Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Position_Salaries.csv')

# Make a matrix feature of the three independent variables
X = dataset.iloc[:,1:2].values
# Create the dependent variable vector
Y = dataset.iloc[:,2].values

# Splitting the dataset into Trainning set and Testing set
'''from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)
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

# Fitting the Regression Model to the dataset
# Create your regressor here

# Predict a new result
Y_pred = regressor.predict(6.5)

# Visualising the Regression result 
plt.scatter(X, Y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_grid, Y, color='red')
plt.plot(X, regressor.predict(X_grid), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
