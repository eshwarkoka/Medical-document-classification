import io
import os
import sys
import shutil
import math
import nltk
import numpy as np
import scipy.sparse as sp
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
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
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn import linear_model
from sklearn.ensemble import ExtraTreesClassifier

#rootdir = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohsumed-all/'
def project_files_combined(path):
	final_result=''
	flist=[]
	rootdir = path
	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	        flist.append(os.path.join(subdir, file))

	fnamelist=[]
	for each in flist:
		fnamelist.append(each[-7:])

	print(len(fnamelist))
	folder_names=os.listdir(rootdir)
	print(folder_names)
	final_result+="Number of folders:	 "+str(len(folder_names))+"\n"
	#final_result+="Folder names : "+' '.join(folder_names)+"\n"
	final_result+="Folder names ------------------ Number of documents\n\n"

	nodlist=[] #number of documents in each directory
	for dir,subdir,files in os.walk(rootdir):
	    if str(len(files))=='0': continue
	    nodlist.append(str(len(files)))

	print(nodlist)
	nod=0
	for each in folder_names:
		final_result+=" "+str(each)+"--------------------------"+nodlist[nod]+"\n"
		nod+=1
	#final_result=final_result[:-2]

	nodlist=list(map(int,nodlist)) #str to int
	total_documents=0
	for each in nodlist:
		total_documents+=each
	print('Total documents---------------'+str(total_documents))
	final_result+="\nTotal documents: "+str(total_documents)+"\n"

	k=0
	c=1
	nodc=nodlist[0] #number of documents in first subdirectory
	loopcount=1
	for each in folder_names:
		exec(each+"=[]")
		for i in range(k,nodc):
			exec(each+'.append(fnamelist[i])')
		#exec('print(len('+each+'))')
		if len(folder_names)==loopcount:
			break
		k=nodc
		nodc+=nodlist[c]
		c+=1
		loopcount+=1

	duplicates=[]
	s=0 #variable restricting repeated combinations
	for each1 in folder_names:
		exec('newlist1=list('+each1+')')
		#print(newlist1)
		s+=1
		for each2 in folder_names[s:]:
			#print(each2)
			newlist2=[]
			#newlist2.clear()
			exec('newlist2=list('+each2+')')
			duplicates.extend(list(set(newlist1)&set(newlist2)))

	duplicates=list(set(duplicates))
	#print(duplicates)
	print('Number of duplicates------------'+str(len(duplicates)))
	final_result+="Number of multi-label documents found: "+str(len(duplicates))+"\n`\n"

	if len(duplicates)==0:
		print('No duplicates found !!!')
		final_result+="No duplicates found !!!\n"
		raise SystemExit

	for each1 in folder_names:
		exec('list1=[]')
		#exec('list1.clear()')
		exec('list1=list('+each1+')')
		#exec(each1+'.clear()')
		exec('del '+each1[:])
		exec(each1+'=[]')
		#exec('print('+each1+')')
		#print(list1)
		#print(len(list1))
		for each2 in list1:
			if each2 not in duplicates:
				#print(each2)
				#list1.remove(each2)
				exec(each1+'.append(each2)')
		#print('-----------After removing duplicates------------')
		#print(list1)
		#exec(each1+'=list(list1)')
		#exec('print('+each1+')')
		#exec('print(len('+each1+'))')
	final_result+="----------------------------After removing multi-label documents------------------------------\n"
	final_result+="Folder names ------------------- Number of documents\n\n"
	lcount=0
	for each in folder_names:
		exec('len_each=len('+each+')')
		final_result+=str(each)+"------------------"+str(len_each)+"\n"
		exec('lcount+=len('+each+')')
	print('-----------Number of single-labelled-documents------------')
	print(lcount)
	final_result+="Total documents: "+str(lcount)+"\n`\n"

	if not os.path.exists('single_label_docs'):
		os.makedirs('single_label_docs')

	for each in folder_names:
		newdir='single_label_docs/'+each
		if not os.path.exists(newdir):
			os.makedirs(newdir)
		oldpath=rootdir+each
		for filename in os.listdir(oldpath):
			filelist=[]
			#filelist.clear()
			exec('filelist=list('+each+')')
			if filename in filelist:
				full_file=rootdir+'/'+each+'/'+filename
				shutil.copy(full_file,newdir)

	print('-------------single_label_docs folder created successfully-----------------')
	final_result+='------------single_label_docs folder created successfully---------------------------\n`\n'
	final_result+="PREPROCESSING IS DONE BELOW"
	stop_words = set(stopwords.words('english')).union(set(list(punctuation)))
	#path = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/flask/single_label_docs/'
	path="single_label_docs/"
	list1=os.listdir(path)
	for each in list1:
		newdir='stopwordremoval+pos/'+each+'/'
		if not os.path.exists(newdir):
			os.makedirs(newdir)
		newpath=path+each+'/'
		for filename in os.listdir(newpath):
			ff=newpath+filename
			file1 = open(ff)
			line = file1.read()
			text_pos = nltk.word_tokenize(line)
			newlist1 = nltk.pos_tag(text_pos)
			newlist2 = []
			#newlist2.clear()
			rellist = ['NNP','JJ','NN','NNS']
			for each2 in newlist1:
				if each2[1] in rellist:
					newlist2.append(each2[0])
			for r in newlist2:
				if not r in stop_words and not r.isdigit() and not r.startswith("(") and not r.endswith(")") and not r.endswith(".") and not r.endswith(",") and not r.endswith(";") and not r.endswith("%") and not r[0].isdigit() and not r.startswith("[") and not r.endswith("]") and not r.startswith("+"):
					fname = newdir+filename
					appendFile=open(fname,'a')
					appendFile.write(r+' ')
					appendFile.close()
		print('stopword-removal-and-pos-tagging---------DONE-----------'+each)

	print('stopword-removal-and-pos-tagging----------------------------DONE------------------')
	final_result+="\n`\n--------stopword-removal-and-pos-tagging----------------------------DONE------------------\n`\n"
	ps=PorterStemmer()
	#path = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/stopwordremoval+pos/'
	path="stopwordremoval+pos/"
	for each in list1:
		newdir='stemming/'+each+'/'
		if not os.path.exists(newdir):
			os.makedirs(newdir)
		newpath=path+each+'/'
		for filename in os.listdir(newpath):
			ff = newpath+filename
			file1 = open(ff)
			line = file1.read()
			words = line.split()
			for r in words:
				fname=newdir+filename
				appendFile=open(fname,'a')
				appendFile.write(ps.stem(r)+' ')
				appendFile.close()
		print('stemming------------DONE-------------'+each)

	print('stemming--------------------------------------------------------------DONE-------------------')
	final_result+="--------stemming--------------------------------------------------------------------DONE-------------------"
	folder="stemming/"
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
	final_result+="\n`\nTF-IDF Matrix created\n"
	print('tf_idf matrix shape: ')
	print(X_train_tfidf.shape)
	final_result+="TF-IDF Matrix Shape: "+str(X_train_tfidf.shape)+"\n`\n"
	final_result+="FEATURE SELECTION AND CLASSIFICATION ALGORITHMS ARE APPLIED BELOW\n`\n"
	final_result+="\n##############################################################\n"
	print('----------Univariate feature selection-----------Naive Bayes Classification--------------------')
	final_result+="--------------Univariate feature selection-----------Naive Bayes Classification--------------------\n"
	kk=100
	for i in range(0,3):
		final_result+="##############################################################\n"
		print('Number of features========================================================'+str(kk))
		final_result+="Number of features: "+str(kk)+"\n"
		X_new=SelectKBest(chi2, k=kk).fit_transform(X_train_tfidf,med.target)
		kk+=100
		X_train, X_test, y_train, y_test = train_test_split(X_new, med.target, test_size=0.3, random_state=0)
		print('shape of training set: ')
		print(X_train.shape)
		final_result+="Shape of training set: "+str(X_train.shape)+"\n"
		print('shape of test set: ')
		print(X_test.shape)
		final_result+="Shape of test set: "+str(X_test.shape)+"\n"
		text_clf_nb=MultinomialNB().fit(X_train,y_train)
		predicted_nb=text_clf_nb.predict(X_test)
		score_nb=np.mean(predicted_nb == y_test)
		print('score of NB: '+str(score_nb))
		final_result+="Score of Naive Bayes: "+str(score_nb)+"\n"
		result_nb=metrics.classification_report(y_test,predicted_nb,target_names=med.target_names)
		print(result_nb)
		final_result+="_________________________________\n"
		final_result+=result_nb
		final_result+="_________________________________\n"
		print('*************************************************************************')
	final_result+="\n##############################################################\n"

	print('-------Univariate feature selection--------------Decision Tree Classification-------------------------------')
	final_result+="-------------Univariate feature selection--------------Decision Tree Classification-------------------------------"
	kk=100
	for i in range(0,3):
	        final_result+="\n##############################################################\n"
	        print('Number of features========================================================'+str(kk))
	        final_result+="Number of features: "+str(kk)+"\n"
	        X_new=SelectKBest(chi2, k=kk).fit_transform(X_train_tfidf,med.target)
	        kk+=100
	        X_train, X_test, y_train, y_test = train_test_split(X_new, med.target, test_size=0.3, random_state=0)
	        print('shape of training set: ')
	        print(X_train.shape)
	        final_result+="Shape of training set: "+str(X_train.shape)+"\n"
	        print('shape of test set: ')
	        print(X_test.shape)
	        final_result+="Shape of test set: "+str(X_test.shape)+"\n"
	        text_clf_dt=tree.DecisionTreeClassifier().fit(X_train,y_train)
	        predicted_dt=text_clf_dt.predict(X_test)
	        score_dt=np.mean(predicted_dt == y_test)
	        print('score of DT: '+str(score_dt))
	        final_result+="Score of Naive Bayes: "+str(score_nb)+"\n"
	        result_dt=metrics.classification_report(y_test,predicted_dt,target_names=med.target_names)
	        print(result_dt)
	        final_result+="_________________________________\n"
	        final_result+=result_nb
	        final_result+="_________________________________\n"
	        print('*************************************************************************')
	        print('Type of result is')
	        print(type(result_dt))        
	final_result+="\n##############################################################"
	final_result=final_result.split('\n')
	return final_result
