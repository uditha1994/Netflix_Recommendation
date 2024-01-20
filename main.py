# import  os
# print(os.getcwd())
# print(os.listdir())
from datetime import date

import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re

data = pd.read_csv("/home/udithal/Downloads/archive/netflixData.csv")
# print(data.head(10))
# print(data.isnull().sum())

# slicing data
data = data[["Title","Description","Content Type","Genres"]]
# print(data.isnull().sum())
# print(data.head())

data = data.dropna()
print(data)

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
