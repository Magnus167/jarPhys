from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from nltk.tokenize import sent_tokenize as splitToSentences
import nltk.corpus
from nltk.corpus import wordnet
import nltk.stem.snowball
import glob
import string
from progress.bar import ChargingBar
import re
import collections
import webbrowser
import os
files = {}
baseDir = './database/'
extractedDirectory = baseDir + 'extracted/'
selectedDir = ''

stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')
tokenizer = nltk.tokenize.WordPunctTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def createHTML(listx,outName, qry, sDir='-1',imgDir='slides/'):
    global selectedDir
    if sDir=='-1':
        sDir=selectedDir
    f = open(outName+'.html','w')
    message = '<html><head><title>jarPhys Output</title></head><body style="background-color:black;" text="#ffffff"><p><h2> Query : '+ qry+'</h2></p>'
    for l in listx:
        message = message + '<p><img src="'+baseDir+imgDir+sDir+'/'+str(l[0])[:-4]+'.png" width=350><span class="caption" style="color:white"> : '+str(l[0])[:-4]+'</span>'
        
    
    message = message + '</body></html>'
    f.write(message)
    f.close()
    



def getDocName(strx):
    a = strx.split("-") 
    return a[0]





def get_wordnet_pos(pos_tag):
    tags = ['J', 'V', 'R', 'N']
    wordnetObjs = [wordnet.ADJ ,wordnet.VERB, wordnet.ADV, wordnet.NOUN]
    if pos_tag[1][0] in tags:
        return (pos_tag[0], wordnetObjs[tags.index(pos_tag[1][0])])
    else:
        return (pos_tag[0], tags[-1])

def lemmae(a):
    pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    return lemmae_a

def compareTokens(a ,b):
    ratio = len(set(lemmae(a)).intersection(lemmae(b))) / float(len(set(lemmae(a)).union(lemmae(b))))
    return int(ratio*100)


def fuzzyExtract(query, strDict, resCount):
    res = []
    keys = strDict.keys()
    res2 = []
    
    bar =  ChargingBar('Searching Files :  ', max=len(keys))
    for key in keys:
        for strx in strDict[key]: 
            #if lemmae(strx)>=lemmae(query):
                #res.append([100-compareTokens(strx, query), strx, key])
            qry = query.split(" ")
            flag = True
            qryStr = '.'.join(strDict[key])
            for q in qry:
                flag = flag and (q in qryStr)
            if flag:
                t = 1
            else:
                t = 101-fuzz.token_set_ratio(query, strx)
            res.append([t, strx, getFileName(key, True)])
        bar.next()
    bar.finish()  
            
    sorted_list = sorted(res, key=lambda x:x[0])
    I = 0
    C = 0
    freqs = [] 
    if resCount>len(sorted_list):
        resCount= len(sorted_list)
    while I<resCount:       
        elem = sorted_list[C]
        C+=1        
        if len(lemmae(elem[1]))>2:
            print(I+1 , ")", chr(9),elem[2], " : ", repr(elem[1]).strip())
            freqs.append(elem[2])
            I += 1            
    
    frqx = collections.Counter(freqs)
    freqs = []
    mx = max(frqx.values())
    for f in frqx:
        freqs.append([f, mx - frqx[f]])
    
    sorted_list = sorted(freqs, key=lambda x:x[1])
    
    print("Most 'interesting' documents : ")
    for d in sorted_list:
        print(d[0])
    createHTML(sorted_list,'results', query)


def getFileName(strx, style=False):
    a = strx.split("\\")    
    if style:
        return a[len(a)-1]
    else:
        a = a[0].split("-")    
        return ('-'.join(a[:len(a)-1]))

def chooseDir(dataBaseDirectory):
    global selectedDir
    folders=[]
    directory_contents = os.listdir(dataBaseDirectory)
    for item in directory_contents:
        if os.path.isdir(dataBaseDirectory  + item):
            folders.append(str(item)) 
    
    print("Choose one of the following folders please : ")
    for f in folders:
        print(' - ', f)    

    while True:
        dirName = input("Folder name : ")
        if (dirName in folders):
            print("Folder selected successfully...")
            selectedDir = dirName
            return str(dataBaseDirectory + dirName+'/*')
            break;
        else:
            print("Please select from one of the above listed folders")   
        




def loadFiles():
    baseFolder =  chooseDir(extractedDirectory)
    global files
    bar =  ChargingBar('Loading Files :  ', max=len(glob.glob(baseFolder)))
    for f in glob.glob(baseFolder):
        with open(f, "r") as infile:
            strs = infile.readlines()
            snts = splitToSentences('.'.join(strs))
            files[getFileName(f, True)] = snts
            bar.next()
    bar.finish()


def searchX(qry, resCount):
    #my_file = open("./extracted/combinedOutput.txt", "r")
    global files

    fuzzyExtract(qry, files, resCount)
    print ('......................................')


def searcherMain():

    loadFiles()
    while True:        
        searchStr = input("enter search query : ")        
        #resNum = input("display n results : ")
        while True:
            try:
                resNum = int(input("display n results : "))    
                break;  
            except ValueError:
                print("Provide an integer value...")
                continue
        searchX(searchStr, int(resNum))
        # syntax = searchX ( query, top n results )
        webbrowser.open_new_tab('results.html')

searcherMain()


