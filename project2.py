import io
import os
import math
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
'''
stop_words = set(stopwords.words('english')).union(set(list(punctuation)))
path = '/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/ohsumed-all/'
list1 = ['C01/','C02/','C03/','C04/','C05/','C06/','C07/','C08/','C09/','C10/','C11/','C12/','C13/','C14/','C15/','C16/','C17/','C18/','C19/','C20/','C21/','C22/','C23/']
#list1 = ['C01/','C02/','C03/']
def hasdigit(inpstring):
     return any(char.isdigit() for char in inpstring)
for each in list1:
	newdir='stopwordremoval/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	newpath=path+each
	for filename in os.listdir(newpath):
		ff=newpath+filename
		#print("\n"+ff)
		file1 = open(ff)
		line = file1.read()
		words = line.split()
		#words = words.lower()
		for r in words:
			if not r in stop_words and not r.isdigit() and not r.startswith("(") and not r.endswith(")") and not r.endswith(".") and not r.endswith(",") and not r.endswith(";") and not r.endswith("%") and not r[0].isdigit() and not r.startswith("[") and not r.endswith("]") and not r.startswith("+") and not hasdigit(r):
				fname='stopwordremoval/'+each+filename
				appendFile=open(fname,'a')
				appendFile.write(" "+r)
				appendFile.close()
	str1 = 'stopword-removal--------------DONE for one folder-------------'+each
	print(str1)
print('stopword-removal------------------------------------------------------DONE------------------')
ps=PorterStemmer()
path = '/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/stopwordremoval/'
for each in list1:
	newdir='stemming/'+each
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	newpath=path+each
	for filename in os.listdir(newpath):
		ff = newpath+filename
		file1 = open(ff)
		line = file1.read()
		words = line.split()
		for r in words:
			fname='stemming/'+each+filename
			appendFile=open(fname,'a')
			appendFile.write(" "+ps.stem(r))
			appendFile.close()
	str2='stemming---------------------DONE for one folder-----------'+each
	print(str2)
print('stemming--------------------------------------------------------------DONE-------------------')

'''
rootdir = '/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/stemming'
flist=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        flist.append(os.path.join(subdir, file))
#print(flist)

print('file list obtained')

line=''
s=set()
#flist=glob.glob(r'/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/ppsamplesm2/*') #get all the files from the d`#open each file >> tokenize the co$
for fname in flist:
    tfile=open(fname,"r")
    line=tfile.read() # read the content of file and store in "line"
    tfile.close() # close the file
    s=s.union(set(line.split(' '))) # union of common words
    #print('common words are united for '+fname)

s=sorted(s) # sorts the content alphabetically
print('All words are sorted')
print('-----------first-iteration-is-done-----------------')
num_of_terms=len(s)
print('\n\n')
print('Number of terms=======')
print(num_of_terms)
print('\n\n')
i=0
ct=0
tf_line=''
doc_counts=[]
count=0
for term in s: #takes each term in the set 
    doc_counts.append(0)
    #print('term------------------------'+term)
    for fdoc in flist: # counts the no of times "term" is encountered in each doc
        doc=open(fdoc)
        line=doc.read()
        doc.close()
        #term=str(term)
        ct=line.count(str(term)) #counts the no. of times "term" is present in the file
        tf_line+=str(ct)+',	' #prints the count in each doc seperated by comma
        if (ct>0):              #counts no of docs in which 
              doc_counts[i]+=1    #this "term" is found
        #print(term+' is searched in document '+fdoc)
    i+=1
    count+=1
    if count%1000==0:
        print('1000 terms iterated')
    tf_line=tf_line.strip()+'\n'    
    #print('completed term-----------'+term)
print('-----------second-iteration-is-done-------------')
idf=[]  #inverse document frequency      
weights=[]      #weight
total_docs=len(flist)   #total number of documents

i=0

# doc_counts = number of documents in which a term is present

'''
print('doc_counts is printed below.......... \n\n\n')
print(doc_counts)
print('\n\n\n')
doc_counts_length=len(doc_counts)
print('length of doc_counts======')
print(doc_counts_length)
num_of_terms=len(s)
print('number of terms=================')
print(num_of_terms)
'''

for doc_count in doc_counts:    #takes the 1st doc count
    idf.append(math.log(total_docs/doc_count)) #calculates idf for each "term"
    weights.append(idf[i]*doc_count) #calculate weight of the term
    #print('weights appended-----'+i)
    i+=1
'''
print('\n\n\n')
print('idf is printed below \n')
print(idf)
print('idf count is printed below \n')
idf_count=len(idf)
print(idf_count)
print('weights are printed below \n')
print(weights)
print('weights count is printed below \n')
weights_count=len(weights)
print(weights_count)
print('\n\n\n')
'''
print('-------------third-iteration-is-done--------------')
final_line='TERM'+','       
i=1
for f in flist:
    final_line+='D'+str(i)+'  '+','
    i+=1
final_line+=','+'IDF'+','+'TF-IDF\n'

print('-----------fourth-iteration-is-done--------------')

tf_arr=tf_line.split('\n')

i=0
for term in s:
    final_line+=term+','+tf_arr[i]+','+str(round(idf[i],2))+','+' '+str(round(weights[i],2))+','+'\n'
    i+=1
    #print('final iteration '+i)
print('------------fifth-iteration-is-done------------FINAL-----')
fdoc="finalresult.csv"
print('output file created--------------finalresult.csv')
outfile=open(fdoc,"w")
outfile.write(final_line)
outfile.close()
print("tf_idf-------------------------------------------DONE")

