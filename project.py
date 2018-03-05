import io
import os
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
stop_words = set(stopwords.words('english')) + list(punctuation)
path = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/ohsumed-all/'
list1 = ['C01/','C02/','C03/','C04/','C05/','C06/','C07/','C08/','C09/','C10/','C11/','C12/','C13/','C14/','C15/','C16/','C17/','C18/','C19/','C20/','C21/','C22/','C23/']
for each in list1:
	newdir='preprocessed/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	newpath=path+each
	for filename in os.listdir(newpath):
		ff = newpath+filename
		#print("\n"+ff)
		file1 = open(ff)
		line = file1.read()
		words = line.split()
		words = words.lower()
		for r in words:
			if not r in stop_words and not r.isdigit():
				fname='preprocessed/'+each+filename
				appendFile=open(fname,'a')
				appendFile.write("\n"+r)
				appendFile.close()
ps=PorterStemmer()
path = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/preprocessed/'
for each in list1:
	newdir='preprocessed2/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	newpath=path+each
	for filename in os.listdir(newpath):
		ff = newpath+filename
		file1 = open(ff)
		line = file1.read()
		words = line.split()
		for r in words:
			fname='preprocessed2/'+each+filename
			appendFile=open(fname,'a')
			appendFile.write("\n"+ps.stem(r))
			appendFile.close()


