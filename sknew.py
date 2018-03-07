import sys
import numpy as np
import scipy.sparse as sp
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files

folder='/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohsumed-all/'
med=load_files(folder, shuffle = False)
print('Target names are printed below: ')
print(med.target_names)
print(len(med.data))
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(med.data)
print('Count Vectorizer shape: ')
print(X_train_counts.shape)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print('shape of tf_idf matrix: ')
print(X_train_tfidf.shape)
print(X_train_tfidf)
sp.save_npz('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/sparse_matrix.npz',X_train_tfidf)
print('************sparse_matrix created and saved successfully**********')
