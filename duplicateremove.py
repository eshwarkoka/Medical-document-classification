import os
import sys
import re
rootdir = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohmfew/'
flist=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        flist.append(os.path.join(subdir, file))

fnamelist=[]
for each in flist:
	fnamelist.append(each[-7:])
print(fnamelist)
folder_list=os.listdir('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohmfew')
print(folder_list)

nodlist=[]
for dir,subdir,files in os.walk('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohmfew/'):
    if str(len(files))=='0': continue
    nodlist.append(str(len(files)))
nodlist=list(map(int,nodlist))
print(nodlist)
k=1
c=0
for each in folder_list:
	exec(each+"=[]")
	for i in range(k,nodlist[c]):
		exec(each.append(flist[i]))
	k=nodlist[c]+1
	c+=1
print(C01)
'''
for i in range(k,nodlist[c]):
	str(each).append(flist[i])
k=nodlist[c]+1
c+=1
print(str(each))
'''
