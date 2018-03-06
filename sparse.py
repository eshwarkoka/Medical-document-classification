import os
import math
import numpy as np
import scipy.sparse as sp
#path = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/pp2/'
#list1 = ['C01/','C02/','C03/','C04/','C05/','C06/','C07/','C08/','C09/','C10/','C11/','C12/','C13/','C14/','C15/','C16/','C17/','C18/','C19/','C20/','C21/','C22/','C23/']
list1 = ['C01/','C02/','C03/']
row_list=[]
col_list=[]
data_list=[]
lcount=0
tf=[]
idf=[]
dcwt=0
#nod=[]
nodcount=0
#doc_count_with_t=[]
main_col_count=0
main_doc_count=0
row_list_count=0
col_list_count=-1
for each in list1:
	doc_count_with_t=[]
	rootdir = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/pp2/'
	rootdir=rootdir+each
	flist=[]
	#print(rootdir)
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			flist.append(os.path.join(subdir, file))
	#print(flist)
	#mainlist=[]
	#tf=[]
	#idf=[]
	nodcount=0 #number of documents
	for each in flist:
		row_list_count+=1
		filelist=[]
		openf = open(each,"r")
		line = openf.read()
		openf.close()
		filelist=line.split()
		#print(filelist)
		#print('********************************')
		for each2 in filelist:
			row_list.append(row_list_count)
			col_list_count+=1
			col_list.append(col_list_count)
			c = filelist.count(each)
			#print(c,sep=' ')
			l = len(filelist)
			#print(l,sep='\t')
			tfval=c/l
			tf.append(round(tfval,2))
			#mainlist.append(each2)
			dcount=0
			for each3 in flist:
				opene3 = open(each3,"r")
				linee3 = opene3.read()
				opene3.close()
				each3flist=[]
				each3flist=linee3.split()
				if each2 in each3flist:
					dcount+=1
					#doc_count_with_t[dcwt]+=1
			doc_count_with_t.append(dcount)
			#dcwt+=1
		nodcount+=1
	#nod.append(nodcount)
	#main_doc_count+=nod
	#print(nod)
	#nodwitht=0
	for dc in doc_count_with_t:
		idf.append(round(math.log(nodcount/dc),2))
	'''
	for each in mainlist:
		nodwitht=0
		#row_list_count+=1
		countlist=[]
		for ff in flist:
			openf = open(ff,"r")
			line = openf.read()
			openf.close()
			countlist=line.split()
			#print('countlist is printed below')
			#print(countlist)
			if each in countlist:
				nodwitht+=1
		idf.append(round(math.log(nod/nodwitht),2))
	#print('Length of main list: ')
	#print(len(mainlist))
	'''
	#main_col_count+=len(mainlist)
	print('---------------tf_idf--------done for one folder-------------------------'+list1[lcount])
	lcount+=1

#print(idf)
#print(len(doc_count_with_t))
#print(doc_count_with_t)
print(len(tf))
print(len(idf))
print(len(row_list))
print(len(col_list))
#print('main_doc_count: ')
#print(main_doc_count)
#print('main_col_count: ')
#print(main_col_count)
#print(idf)
#data_list=[a*b for a,b in zip(row_list,col_list)]
from operator import mul
data_list_temp=[]
data_list_temp=list(map(mul,tf,idf))
data_list=[round(ele,2) for ele in data_list_temp]
#print(data_list)
#print(row_list)
sparse_matrix = sp.csr_matrix((data_list,(row_list,col_list)),shape=(main_doc_count+1,main_col_count))
#print(arr)
sp.save_npz('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/sparse_matrix.npz',sparse_matrix)
print('************sparse_matrix created and saved successfully**********')
