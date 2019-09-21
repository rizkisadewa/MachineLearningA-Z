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
nltk.download('stopwords')
from nltk.corpus import stopwords
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])
review = review.lower()
review = review.split()
review = [word for word in review if not word in set(stopwords.words('english'))]