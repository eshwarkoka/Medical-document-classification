import os
import sys
import shutil
import io
import copy
import math
import nltk
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
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from flask import Flask, request, Response, render_template, redirect, url_for
import project as pr

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
	path = request.form['path']
	fresult=pr.project_files_combined(path)
	return render_template('result.html',name=fresult)

if __name__ == "__main__":
	app.debug=True
	app.run(debug=True)


#/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/flask/ohmfew/