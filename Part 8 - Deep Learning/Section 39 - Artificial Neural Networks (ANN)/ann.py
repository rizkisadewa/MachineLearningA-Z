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

# Splitting the dataset into Trainning set and Testing set
from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 0)

'''
the remark will be updated soon
'''

# Feature Scaling

from sklearn.preprocessing import StandardScaler # import class from library
sc_X = StandardScaler() # an object from the class above
X_train = sc_X.fit_transform(X_train) # fit the object and transform it 
X_test = sc_X.transform(X_test) # we only transfer the object as it's already fitted in train set

'''
for the dependent variable vector do not have to be scalled due to the the value represent
as category with 2 value "yes" or "no"
'''

# Fitting Classifier to the Trainning set
# Create your Classfication

# Predicting the Test set results
Y_pred = classifier.predict(X_test)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, Y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Importing the keras libraries and packages 
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the Ann