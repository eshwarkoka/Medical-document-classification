import io
import os
import math
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
stop_words = set(stopwords.words('english')).union(set(list(punctuation)))
#path = '/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/ohsumed-all/'
#list1 = ['C01/','C02/','C03/','C04/','C05/','C06/','C07/','C08/','C09/','C10/','C11/','C12/','C13/','C14/','C15/','C16/','C17/','C18/','C19/','C20/',$
x=input("1. Enter 1 for Windows \n2. Enter 2 for Linux : \n")
print(x)
if x=='1':
    path=input("Enter the path of the target folder \n NOTE: If \\u is a part of the path, then use double back-slash a path separator: ")
    list1=os.listdir(path)
    #print(list1)
elif x=='2':
    path=input("Enter the path of the target folder : ")
    list1=os.listdir(path)
    #print(list1)else:
else:
    print("Invalid Entry !!")
print(list1)

