import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
import numpy
import scipy.sparse as sp
folder='/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohsumed-all/'
#sklearn.datasets.load_files('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/ohmfew/')
med=load_files(folder, shuffle = False)
print('Target names are printed below: ')
print(med.target_names)
print(len(med.data))
#print(datasets)
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(med.data)
print('Count Vectorizer shape: ')
print(X_train_counts.shape)
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print('shape of tf_idf matrix: ')
print(X_train_tfidf.shape)
print(X_train_tfidf)
sp.save_npz('/media/eshwar/DATA/Eshwar/Projects/Text classification/Medical-document-classification/sparse_matrix.npz',X_train_tfidf)
print('************sparse_matrix created and saved successfully**********')
'''
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, med.target)
docs_new=[' small anim model human helicobact pylori activ chronic gastriti isol spiral-shap bacterium helicobact pylori cat stomach possibl new small anim model gastric infect pure bacterium helicobact feli germ-fre mice organ stomach larg number mucu deep gastric pit gastric trophism pylori signific histopatholog felis-infect mice week postinfect acut inflammatori respons eosinophil neutrophil week polymorphonuclear respons pronounc larg number neutrophil area small microabscess lymphocyt number week sever larg lymphoid nodul present submucosa multipl small microabscess present pylor mucosa first anim model bacteri gastriti progress acut inflamm persist acut chronic inflamm activ chronic human infect pylori',' albuterol acut bronchiol double-blind placebo-control trial infant week month age first episod wheez sign symptom bronchiol albuterol mg/kg/dose placebo salin solut administr hour albuterol therapi improv accessori muscl score vs oxygen satur vs dose accessori muscl score vs respiratori rate vs oxygen satur vs dose drug respons therapi similar infant month age heart rate albuterol group baselin placebo group side effect treatment children nasal specimen swab viral identif posit test result respiratori syncyti viru parainfluenza paramyxoviru influenza nebul albuterol safe effect treatment infant bronchiol',' high infecti morbid pregnant women insulin-depend diabet underst complic patient insulin-depend diabet prone infect poor metabol control rel immun defici exist pregnanc pregnant patient insulin-depend diabet risk infect infect poor glycem control pregnant women insulin-depend diabet nondiabet pregnant control episod infect deliveri women insulin-depend diabet control group rate postpartum infect time group insulin-depend diabet suscept kind infect overal differ indic glycem control hemoglobin infect infect high rate infect exist pregnant women diabet infect poor glycem control unclear improv metabol control high infect rate']
X_new_counts=count_vect.transform(docs_new)
X_new_tfidf=tfidf_transformer.transform(X_new_counts)
predicted=clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
	print(med.target_names[category])
'''
