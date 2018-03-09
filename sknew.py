import sys
import numpy as np
import scipy.sparse as sp
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import tree
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files

folder='/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/pp2/'
med=load_files(folder, shuffle = False)
#print(med)
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
#sp.save_npz('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/sparse_matrix.npz',X_train_tfidf)
#print('************sparse_matrix created and saved successfully**********')

X_train, X_test, y_train, y_test = train_test_split(X_train_tfidf, med.target, test_size=0.3, random_state=0)

'''
print('shape of training set')
#print(X_train)
print('shape of test set')
#print(X_test)
print('----------------------')
print(y_train)
print('----------------------')
print(y_test)

lm=linear_model.LinearRegression()
model=lm.fit(X_train, y_train)
predictions=lm.predict(X_test)
print(predictions)
score=model.score(X_test,y_test)
print('score: '+str(score))
'''

text_clf_nb=MultinomialNB().fit(X_train,y_train)
predicted_nb=text_clf_nb.predict(X_test)
score_nb=np.mean(predicted_nb == y_test)
print('score of NB: '+str(score_nb))

text_clf_dt=tree.DecisionTreeClassifier().fit(X_train,y_train)
predicted_dt=text_clf_dt.predict(X_test)
score_dt=np.mean(predicted_dt == y_test)
print('score of DT: '+str(score_dt))

text_clf_onevsrest=OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train,y_train)
print(text_clf_onevsrest)
predicted_ovr=text_clf_onevsrest.predict(X_test)
score_ovr=np.mean(predicted_ovr == y_test)
print('score of onevsrestclassifier: '+str(score_ovr))
