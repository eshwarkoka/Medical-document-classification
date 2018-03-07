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

folder_names=os.listdir(rootdir)
print(folder_names)

nodlist=[] #number of documents in each directory
for dir,subdir,files in os.walk(rootdir):
    if str(len(files))=='0': continue
    nodlist.append(str(len(files)))

nodlist=list(map(int,nodlist)) #str to int
print(nodlist)

total_documents=0
for each in nodlist:
	total_documents+=each
print('Total documents---------------'+str(total_documents))

k=0
c=1
nodc=nodlist[0] #number of documents in first subdirectory
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

duplicates=[]
s=1 #variable restricting repeated combinations
for each1 in folder_names:
	exec('newlist1=list('+each1+')')
	for each2 in folder_names[s:]:
		exec('newlist2=list('+each2+')')
		duplicates.extend(list(set(newlist1)&set(newlist2)))
	s+=1

print(duplicates)
print('Number of duplicates------------'+str(len(duplicates)))
