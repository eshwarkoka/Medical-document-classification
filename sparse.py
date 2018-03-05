import os
import math
import numpy as np
import scipy.sparse as sp
path = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/pp2/'
list1 = ['C01/','C02/','C03/']
row_list=[]
col_list=[]
data_list=[]
tf=[]
idf=[]
maincount=0
maindoccount=0
row_list_count=0
col_list_count=0
for each in list1:
	rootdir = '/media/eshwar/DATA/Eshwar/Projects/meddocclproject/pp2/'
	rootdir=rootdir+each
	flist=[]
	#print(rootdir)
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			flist.append(os.path.join(subdir, file))
	#print(flist)
	mainlist=[]
	#tf=[]
	#idf=[]
	nod=0 #number of documents
	for each in flist:
		row_list_count+=1
		filelist=[]
		openf = open(each,"r")
		line = openf.read()
		openf.close()
		filelist=line.split()
		#print(filelist)
		#print('********************************')
		for each in filelist:
			row_list.append(row_list_count)
			col_list_count+=1
			col_list.append(col_list_count)
			c = filelist.count(each)
			l = len(filelist)
			tfval=c/l
			tf.append(round(tfval,2))
			mainlist.append(each)
		nod+=1
	maindoccount+=nod
	nodwitht=0
	for each in mainlist:
		#row_list_count+=1
		countlist=[]
		for ff in flist:
			openf = open(ff,"r")
			line = openf.read()
			openf.close()
			countlist=line.split()
			if each in countlist:
				nodwitht+=1
				continue
		idf.append(round(math.log(nod/nodwitht),2))
	#print('Length of main list: ')
	#print(len(mainlist))
	#maincount+=len(mainlist)
	print('---------------------------------------------')
print(len(tf))
print(len(idf))
print(len(row_list))
print(len(col_list))
#print(idf)
#data_list=[a*b for a,b in zip(row_list,col_list)]
from operator import mul
data_list=list(map(mul,tf,idf))
print(len(data_list))
#print(row_list)
arr = sp.csr_matrix((data_list,(row_list,col_list)),shape=(5000,5000))
print(arr)
