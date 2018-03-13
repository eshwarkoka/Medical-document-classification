import sys
import numpy as np
import scipy.sparse as sp
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
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
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier

folder='/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/stemming/'
med=load_files(folder, shuffle = False)
print('Target names are printed below: ')
print(med.target_names)
print('Length of data is printed below: ')
print(len(med.data))
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(med.data)
print('Count Vectorizer shape: ')
print(X_train_counts.shape)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print('tf_idf matrix shape: ')
print(X_train_tfidf.shape)

#print(X_train_tfidf)
#sp.save_npz('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/sparse_matrix.npz',X_train_tfidf)
#print('************sparse_matrix created and saved successfully**********')


print('----------Univariate feature selection-----------Naive Bayes Classification--------------------')
kk=500
for i in range(0,6):
	print('Number of features========================================================'+str(kk))
	X_new=SelectKBest(chi2, k=kk).fit_transform(X_train_tfidf,med.target)
	kk+=500
	X_train, X_test, y_train, y_test = train_test_split(X_new, med.target, test_size=0.3, random_state=0)
	print('shape of training set: ')
	print(X_train.shape)
	print('shape of test set: ')
	print(X_test.shape)
	text_clf_nb=MultinomialNB().fit(X_train,y_train)
	predicted_nb=text_clf_nb.predict(X_test)
	score_nb=np.mean(predicted_nb == y_test)
	print('score of NB: '+str(score_nb))
	print(metrics.classification_report(y_test,predicted_nb,target_names=med.target_names))
	print('*************************************************************************')

print('-------Univariate feature selection--------------Decision Tree Classification-------------------------------')
kk=500
for i in range(0,6):
        print('Number of features========================================================'+str(kk))
        X_new=SelectKBest(chi2, k=kk).fit_transform(X_train_tfidf,med.target)
        kk+=500
        X_train, X_test, y_train, y_test = train_test_split(X_new, med.target, test_size=0.3, random_state=0)
        print('shape of training set: ')
        print(X_train.shape)
        print('shape of test set: ')
        print(X_test.shape)
        text_clf_dt=tree.DecisionTreeClassifier().fit(X_train,y_train)
        predicted_dt=text_clf_dt.predict(X_test)
        score_dt=np.mean(predicted_dt == y_test)
        print('score of DT: '+str(score_dt))
        print(metrics.classification_report(y_test,predicted_dt,target_names=med.target_names))
        print('*************************************************************************')



'''
text_clf_dt=tree.DecisionTreeClassifier().fit(X_train,y_train)
predicted_dt=text_clf_dt.predict(X_test)
score_dt=np.mean(predicted_dt == y_test)
print('score of DT: '+str(score_dt))
#print(metrics.classification_report(y_test,predicted_dt,target_names=med.target_names))

X_new = SelectKBest(chi2, k=300).fit_transform(X_train_tfidf,med.target)
print('---------------------------')
print(X_new)
print(X_new.shape)


text_clf_nb=MultinomialNB().fit(X_train,y_train)
predicted_nb=text_clf_nb.predict(X_test)
score_nb=np.mean(predicted_nb == y_test)
print('score of NB: '+str(score_nb))
print(metrics.classification_report(y_test,predicted_nb,target_names=med.target_names))




from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

clf = ExtraTreesClassifier()
clf = clf.fit(X_train_tfidf, med.target)
clf.feature_importances_
print(clf)
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X_train_tfidf)
print(X_new.shape)


text_clf_nb=MultinomialNB().fit(X_train,y_train)
predicted_nb=text_clf_nb.predict(X_test)
score_nb=np.mean(predicted_nb == y_test)
print('score of NB: '+str(score_nb))
print(metrics.classification_report(y_test,predicted_nb,target_names=med.target_names))
#print(metrics.precision_recall_fscore_support(y_test,predicted_nb,average=None,labels=med.target_names))

text_clf_dt=tree.DecisionTreeClassifier().fit(X_train,y_train)
predicted_dt=text_clf_dt.predict(X_test)
score_dt=np.mean(predicted_dt == y_test)
print('score of DT: '+str(score_dt))
#print(metrics.classification_report(y_test,predicted_dt,target_names=med.target_names))

text_clf_onevsrest=OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train,y_train)
print(text_clf_onevsrest)
predicted_ovr=text_clf_onevsrest.predict(X_test)
score_ovr=np.mean(predicted_ovr == y_test)
print('score of onevsrestclassifier: '+str(score_ovr))
#print(metrics.classification_report(y_test,predicted_ovr,target_names=med.target_names))

print('--------------Univariate feature selection--------------')
X_new = SelectKBest(chi2, k=300).fit_transform(X_train_tfidf,med.target)
print(X_new)
print('---------------------------')
print(X_new.shape)

print('----------linear model---------------------')
lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X_train_tfidf, med.target)
model = SelectFromModel(lsvc, prefit=True)
X_new_l1 = model.transform(X_train_tfidf)
print(X_new_l1.shape)

print('----------------Tree-------------------')
clf_tree = ExtraTreesClassifier()
clf_tree = clf_tree.fit(X_train_tfidf, med.target)
print(clf_tree.feature_importances_)

model = SelectFromModel(clf_tree, prefit=True)
X_new_tree = model.transform(X_train_tfidf)
print(X_new_tree.shape)

from sklearn import svm
clf = svm.SVC()
clf=clf.fit(X_train_tfidf,med.target)  
print(clf)
'''
