import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

file1 = open("/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/ohsumed-all/C01/0000011")
file2 = open("/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/ohsumed-all/C01/0000021")
file3 = open("/media/eshwar/DATA1/Eshwar/Projects/meddocclproject/ohsumed-all/C01/0000033")
line1 = file1.read()
line2 = file2.read()
line3 = file3.read()
filelist = [line1, line2, line3]
#bloblist = [document1, document2, document3]
for i, blob in enumerate(filelist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, filelist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


