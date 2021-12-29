from __future__ import division
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer


ps = PorterStemmer()
stopwords = set(stopwords.words('english'))
fdist = FreqDist()
milton =  nltk.corpus.gutenberg.words('milton-paradise.txt')
whiteman =  nltk.corpus.gutenberg.words('whitman-leaves.txt')
tokenizer = RegexpTokenizer(r'\w+')

def compare(doc1,doc2):
    stopwordsNumber,pos,tokens,afterStem = getInfo(doc1)
    stopwordsNumber2,pos2,tokens2,afterStem2 = getInfo(doc2)
    print("______first document information______ \n")
    printer(stopwordsNumber,pos,tokens,afterStem)
    print("______second document information______ \n")
    printer(stopwordsNumber2,pos2,tokens2,afterStem2)
    if stopwordsNumber > stopwordsNumber2 :
        print('stopwords number in the first doc is bigger than the secound doc')
    else:
        print('stopwords number in the secound doc is bigger than the first doc')
    print('------------------------------')

def printer(stopwordsNumber,pos,tokens,afterStem):
    print("number of the stop words : ", end = '')
    print(stopwordsNumber)
    print("POS : ", end = '')
    print(pos)
    print("tokens : ", end = '')
    print(tokens)
    print("afterStem : ", end = '')
    print(afterStem)
    print("\n...DONE")
    print('------------------------------')



def getInfo(doc):
    text =""
    stopwordsNumber = 0
    for word in doc[:100]:
        if word not in stopwords:
            text = text +" "+ word
        else:stopwordsNumber +=1
    tokens = tokenizer.tokenize(text)
    pos = nltk.pos_tag(tokens);
    afterStem = ""
    for word in tokens:
        fdist[word.lower()]+=1
        afterStem = afterStem+" "+ps.stem(word)
    return stopwordsNumber,pos,tokens,afterStem


compare(milton,whiteman)
