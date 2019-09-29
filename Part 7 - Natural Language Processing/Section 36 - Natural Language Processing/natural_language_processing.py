# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:13:01 2019

@author: rizky
"""

# Natural Language Processing 
# Importing the libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# import the dataset 
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting = 3)

# Cleaning the texts
import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Create the Bag of words model 
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values


# Classification with Naive Bayes
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Fitting classifier to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# MAKING OWN PREDICTION
X_train_str, X_test_str, y_train_str, y_test_str = train_test_split(corpus, y, test_size = 0.20, random_state = 0)
X_train2 = cv.fit_transform(X_train_str).toarray()
X_test2 = cv.fit_transform(X_test_str).toarray()

# Fitting classifier to the Training set
from sklearn.naive_bayes import GaussianNB
classifier2 = GaussianNB()
classifier2.fit(X_train2, y_train2)

# Predicting the Test set results
y_pred2 = classifier2.predict(X_test2)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(y_test2, y_pred2)