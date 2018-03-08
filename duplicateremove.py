import os
import sys
import shutil

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
	#print(newlist1)
	for each2 in folder_names[s:]:
		exec('newlist2=list('+each2+')')
		duplicates.extend(list(set(newlist1)&set(newlist2)))
	s+=1

duplicates=list(set(duplicates))
#print(duplicates)
print('Number of duplicates------------'+str(len(duplicates)))

for each1 in folder_names:
	exec('list1=[]')
	exec('list1.clear()')
	exec('list1=list('+each1+')')
	exec(each1+'.clear()')
	#exec('print('+each1+')')
	#print(list1)
	#print(len(list1))
	for each2 in list1:
		if each2 in duplicates:
			#print(each2)
			list1.remove(each2)
	#print('-----------After removing duplicates------------')
	#print(list1)
	exec(each1+'=list(list1)')
	#exec('print('+each1+')')
	#exec('print(len('+each1+'))')

lcount=0
for each in folder_names:
	exec('print(len('+each+'))')
	exec('lcount+=len('+each+')')
print('-------------------------------------------')
print(lcount)

if not os.path.exists('single_label_docs'):
	os.makedirs('single_label_docs')

for each in folder_names:
	newdir='single_label_docs/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	oldpath=rootdir+each
	for filename in os.listdir(oldpath):
		exec('filelist=list('+each+')')
		if filename in filelist:
			full_file=rootdir+'/'+each+'/'+filename
			shutil.copy(full_file,newdir)

print('-------------single_label_docs folder successfully created-----------------')

