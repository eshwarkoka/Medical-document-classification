
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
'''
vect = TfidfVectorizer(input='/media/eshwar/DATA/Eshwar/Projects/meddocclproject/ohmfew/C01/0000011')
#X = vect.fit_transform(list_of_filenames)
'''
rootdir = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/pp2/'
flist=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        flist.append(os.path.join(subdir, file))
# list of text documents
text = ["The quick brown fox jumped over the lazy dog.",
		"The dog.",
		"The fox"]
i=0
newlist=[]
for each in flist:
	fileopen = open(each)
	fileread = fileopen.read()
	#print(fileread)
	newlist.append(fileread)
	i+=1
#for each in newlist:
#	print(each)
#	print("\n-------------------------------------------------------------------\n")
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(newlist)
# summarize
print(vectorizer.vocabulary_)
#print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([newlist[0]])
# summarize encoded vector
print(vector.shape)
print(vector.toarray())
np.savetxt("newcsv.csv",vector.toarray(),delimiter=",")
