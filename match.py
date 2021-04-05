import nltk.corpus
from nltk.corpus import wordnet
import nltk.tokenize.punkt
from nltk.tokenize import sent_tokenize
import nltk.stem.snowball
import string
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#from testsent import target_sentence, sentences

# https://bommaritollc.com/2014/06/12/fuzzy-match-sentences-python/ ;


stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')


def splitToSentences(strx):
    return sent_tokenize(strx)



def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

tokenizer = nltk.tokenize.WordPunctTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def fuzzyExtract(query, strArray):
    return process.extract(query, strArray)
    #https://www.geeksforgeeks.org/fuzzywuzzy-python-library/


def fuzzyMatcher(a, b):
    #return fuzz.token_sort_ratio(a, b)
    return fuzz.token_set_ratio(a, b)

def matcher(a, b):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    return (ratio)

def searchInText(inText, qText):
    txt = splitToSentences(inText)
    chunks = [0]
    res = []
    print ("made it")    
    for I in range(0, len(txt)):
        m = matcher(qText, txt[i])
        res.append([m, txt[I]])
      
    sRes = sorted(res, key=lambda x:x[0])
    return sRes
             


        

