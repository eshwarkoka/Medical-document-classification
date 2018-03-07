import os
import sys
import re
rootdir = '/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohsumed-all/'
flist=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        flist.append(os.path.join(subdir, file))

fnamelist=[]
for each in flist:
	fnamelist.append(each[-7:])
#print(fnamelist)
folder_names=os.listdir(rootdir)
print(folder_names)

nodlist=[]
for dir,subdir,files in os.walk(rootdir):
    if str(len(files))=='0': continue
    nodlist.append(str(len(files)))

nodlist=list(map(int,nodlist))
print(nodlist)
k=0
c=1
nodc=nodlist[0]
#print(len(folder_names))
loopcount=1
for each in folder_names:
	exec(each+"=[]")
	for i in range(k,nodc):
		exec(each+'.append(fnamelist[i])')
	if len(folder_names)==loopcount: 
		break
	k=nodc
	nodc+=nodlist[c]
	c+=1
	loopcount+=1
'''
print(C01)
print('--------------------------')
print(C02)
print('-----------------------')
print(C03)
'''
for each in folder_names:
	print(each)
	exec('print('+each+')')
