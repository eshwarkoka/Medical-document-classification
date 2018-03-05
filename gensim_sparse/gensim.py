'''
from gensim import Corpora
class MyCorpus(object):
	def __iter__(self):
		for line in open('/media/eshwar/DATA/Eshwar/Projects/main project/pp2/C01/0000011'):
			yield dictionary.doc2bow(line.lower().split())
corpus_memory_friendly = MyCorpus()
print(corpus_memory_friendly)
for vector in corpus_memory_friendly:
	print(vector)
'''

