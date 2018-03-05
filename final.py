import io
import os
import math
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
stop_words = set(stopwords.words('english')).union(set(list(punctuation)))
path = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/ohmfew/'
#list1 = ['C01/','C02/','C03/','C04/','C05/','C06/','C07/','C08/','C09/','C10/','C11/','C12/','C13/','C14/','C15/','C16/','C17/','C18/','C19/','C20/','C21/','C22/','C23/']
list1 = ['C01/','C02/','C03/']
def hasdigit(inpstring):
     return any(char.isdigit() for char in inpstring)
count=1
for each in list1:
	newdir='pp1/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	newpath=path+each
	for filename in os.listdir(newpath):
		ff=newpath+filename
		#print("\n"+ff)
		file1 = open(ff)
		line = file1.read()
		text_pos = nltk.word_tokenize(line)
		newlist1 = nltk.pos_tag(text_pos)
		#nf = newdir+filename+str('_pos')
		#newfile = open(nf,'a')
		newlist2 = []
		rellist = ['NNP','JJ','NN','NNS']
		for each in newlist1:
			if each[1] in rellist:
				#newfile = open(nf,'a')
				#newfile.write("\n"+str(each))
				#newfile.close()
				newlist2.append(each[0])
			else: continue 
		#words = line.split()
		for r in newlist2:
			if not r in stop_words and not r.isdigit() and not r.startswith("(") and not r.endswith(")") and not r.endswith(".") and not r.endswith(",") and not r.endswith(";") and not r.endswith("%") and not r[0].isdigit() and not r.startswith("[") and not r.endswith("]") and not r.startswith("+") and not hasdigit(r):
				fname = newdir+filename
				appendFile=open(fname,'a')
				appendFile.write(" "+r)
				appendFile.close()
	str1 = 'stopword-removal--------------DONE for one folder-------------'
	print(str1)
	print(count)
	count+=1
print('stopword-removal------------------------------------------------------DONE------------------')
#list1=['C01/','C02/','C03/']
ps=PorterStemmer()
path = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/pp1/'
count2=1
for each in list1:
	newdir='pp2/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	newpath=path+each
	for filename in os.listdir(newpath):
		ff = newpath+filename
		file1 = open(ff)
		line = file1.read()
		words = line.split()
		for r in words:
			fname='pp2/'+each+filename
			appendFile=open(fname,'a')
			appendFile.write(" "+ps.stem(r))
			appendFile.close()
	str2='stemming---------------------DONE for one folder-----------'
	print(str2)
	print(count2)
	count2+=1
print('stemming--------------------------------------------------------------DONE-------------------')
