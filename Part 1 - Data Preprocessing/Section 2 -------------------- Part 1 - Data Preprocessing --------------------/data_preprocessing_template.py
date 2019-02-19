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

# Splitting the dataset into Trainning set and Testing set
from sklearn.model_selection import train_test_split # a library for splitting a dataset
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)
