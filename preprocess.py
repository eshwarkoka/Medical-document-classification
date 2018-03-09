import io
import os
import math
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english')).union(set(list(punctuation)))
path = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/single_label_docs/'

def hasdigit(inpstring):
     return any(char.isdigit() for char in inpstring)

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
		newlist2.clear()
		rellist = ['NNP','JJ','NN','NNS']
		for each2 in newlist1:
			if each2[1] in rellist:
				newlist2.append(each2[0])
		for r in newlist2:
			if not r in stop_words and not r.isdigit() and not r.startswith("(") and not r.endswith(")") and not r.endswith(".") and not r.endswith(",") and not r.endswith(";") and not r.endswith("%") and not r[0].isdigit() and not r.startswith("[") and not r.endswith("]") and not r.startswith("+") and not hasdigit(r):
				fname = newdir+filename
				appendFile=open(fname,'a')
				appendFile.write(r+' ')
				appendFile.close()
	print('stopword-removal-and-pos-tagging---------DONE-----------'+each)

print('stopword-removal-and-pos-tagging----------------------------DONE------------------')

ps=PorterStemmer()
path = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/stopwordremoval+pos/'

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
