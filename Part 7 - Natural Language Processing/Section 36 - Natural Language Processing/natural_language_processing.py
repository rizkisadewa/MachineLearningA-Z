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


