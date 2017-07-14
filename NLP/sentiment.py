import csv
import re
from pathlib import Path
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

file = open('stopwords.en.txt','r') 
stopArr=file.read().splitlines()

c=0

with open('imdb_tr.csv', 'a',encoding='utf-8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL,skipinitialspace=True)
    spamwriter.writerow(['row_number','text','polarity'])    

for i in range(12500):
    for j in range(7,11):
        my_file = Path('../resource/asnlib/public/aclImdb/train/pos/'+str(i)+'_'+str(j)+'.txt')
        if my_file.is_file():           
            file = open('../resource/asnlib/public/aclImdb/train/pos/'+str(i)+'_'+str(j)+'.txt','r',encoding="utf-8") 
            str1=file.read()
            arr1=[w for w in re.split('\W', str1) if w]
            str2=" ".join(str(x) for x in arr1)
            str2=str2.lower()
            str3 = ' '.join([word for word in str2.split() if word not in stopArr])
            with open('imdb_tr.csv', 'a',encoding='utf-8', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL,skipinitialspace=True)
                spamwriter.writerow([str(c),str3,'1'])            
            file.close()
            c+=1
            break

for i in range(12500):
    for j in range(5):
        my_file = Path('../resource/asnlib/public/aclImdb/train/neg/'+str(i)+'_'+str(j)+'.txt')
        if my_file.is_file():
            file = open('../resource/asnlib/public/aclImdb/train/neg/'+str(i)+'_'+str(j)+'.txt','r',encoding="utf-8") 
            str1=file.read()
            arr1=[w for w in re.split('\W', str1) if w]
            str2=" ".join(str(x) for x in arr1)
            str2=str2.lower()
            str3 = ' '.join([word for word in str2.split() if word not in stopArr])
            with open('imdb_tr.csv', 'a',encoding='utf-8', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL,skipinitialspace=True)
                spamwriter.writerow([str(c),str3,'0'])
            file.close()
            c+=1
            break

train = pd.read_csv("imdb_tr.csv", header=0,delimiter=",",encoding='utf-8')
vectorizer1 = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,ngram_range=(1,1))
vectorizer2 = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,ngram_range=(1,2))
vectorizer3 = TfidfVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,ngram_range=(1,1))
vectorizer4 = TfidfVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,ngram_range=(1,2))
train_data_features1 = vectorizer1.fit_transform(train["text"])
train_data_features2 = vectorizer2.fit_transform(train["text"])
train_data_features3 = vectorizer3.fit_transform(train["text"])
train_data_features4 = vectorizer4.fit_transform(train["text"])
clf1 = SGDClassifier(loss="hinge", penalty="l1")
clf1.fit(train_data_features1, train["polarity"])
clf2 = SGDClassifier(loss="hinge", penalty="l1")
clf2.fit(train_data_features2, train["polarity"])
clf3 = SGDClassifier(loss="hinge", penalty="l1")
clf3.fit(train_data_features3, train["polarity"])
clf4 = SGDClassifier(loss="hinge", penalty="l1")
clf4.fit(train_data_features4, train["polarity"])

test = pd.read_csv("../resource/asnlib/public/imdb_te.csv",encoding='latin-1',header=0)
clean_test=[]
for i in range(len(test['text'])):
    arr1=[w for w in re.split('\W', test['text'][i]) if w]
    str2=" ".join(str(x) for x in arr1)
    str2=str2.lower()
    str3 = ' '.join([word for word in str2.split() if word not in stopArr])
    clean_test.append(str3)

test_data_features1 = vectorizer1.transform(clean_test)
test_data_features2 = vectorizer2.transform(clean_test)
test_data_features3 = vectorizer3.transform(clean_test)
test_data_features4 = vectorizer4.transform(clean_test)

result1 = clf1.predict(test_data_features1)
result2 = clf2.predict(test_data_features2)
result3 = clf3.predict(test_data_features3)
result4 = clf4.predict(test_data_features4)

f = open('unigram.output.txt', 'a')
for i in range(len(result1)):
	if str(result1[i])!='polarity':
            f.write(str(result1[i])+'\n')  
f.close()

f = open('unigramtfidf.output.txt', 'a')
for i in range(len(result2)):
	if str(result2[i])!='polarity':
            f.write(str(result2[i])+'\n')  
f.close()

f = open('bigram.output.txt', 'a')
for i in range(len(result3)):
	if str(result3[i])!='polarity':
            f.write(str(result3[i])+'\n')  
f.close()

f = open('bigramtfidf.output.txt', 'a')
for i in range(len(result4)):
	if str(result4[i])!='polarity':
            f.write(str(result4[i])+'\n')  
f.close()
