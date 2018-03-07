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
duplicates=[]
oc=0
ic=0
s=1
for each1 in folder_names:
	oc+=1
	#print(each)
	#exec('print('+each+')')
	exec('newlist1=list('+each1+')')
	#print(newlist1)
	for each2 in folder_names[s:]:
		ic+=1
		exec('newlist2=list('+each2+')')
		duplicates.extend(list(set(newlist1)&set(newlist2)))
		#print(duplicates)
	s+=1
print(duplicates)
