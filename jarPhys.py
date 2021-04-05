import os
import slate3k as slate
from match import searchInText
from nltk.tokenize import sent_tokenize as splitToSentences
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from progress.bar import Bar
from progress.spinner import Spinner
import nltk.corpus
from nltk.corpus import wordnet
#import nltk.tokenize.punkt
import nltk.stem.snowball
import string
from match import get_wordnet_pos


stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')
tokenizer = nltk.tokenize.WordPunctTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmae(a):
    pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    return lemmae_a

def compareTokens(a ,b):
    ratio = len(set(lemmae(a)).intersection(lemmae(b))) / float(len(set(lemmae(a)).union(lemmae(b))))
    return (ratio)


def fuzzyExtract(query, strArray):
    return process.extract(query, strArray)

scraped_data = {}
def getPDFFileNames():
    f = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            f.append(filename)
    f.sort(key=str.lower)
    return f

def createCombinedFilePDF():    
    pdfFiles = getPDFFileNames()    
    spinner = Spinner('Loading PDFs ... ')
    for filename in pdfFiles:
        scraped_data[filename] = {}  
        with open(filename,'rb') as f:
            extracted_text = slate.PDF(f)
            spinner.next()
            f.close()
        for I in range(0, len(extracted_text)):
            scraped_data[filename][I] = extracted_text[I]
    
    spinner.finish()
            


def searchFiles(inStrx):
    s = 0
    for I in scraped_data: s += len(scraped_data[I])
    bar = Bar('Processing', max= s)

    for doc in scraped_data.keys():
        for pg in scraped_data[doc].keys():
            tempDict = {}
            sentences = splitToSentences(scraped_data[doc][pg])            
            for i in range(0, len(sentences)):
                tempDict[i] = {}
                tempDict[i] = sentences[i]
                tempDict[i]['p'] = lemmae(sentences[i]) 
    bar.finish()
    
        
     
        
        




createCombinedFilePDF()
#iStr = input("Enter Search Query : ")
searchFiles('' )







"""

strip numbers
create sentences
create paragraphs
search within sentence = stcScore
search within para = paraScore
create similarity tree using stcScore, paraScore
return pageNumbers, docName, match text, paraScore, stcScore
also return a filePath to resultFile, which contains results sorted by match

"""