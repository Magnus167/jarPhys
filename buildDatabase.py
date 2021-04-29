from PIL import Image
import cv2
import pytesseract
from progress.bar import ChargingBar
import os
from skimage.metrics import structural_similarity as ssim
import imutils
from pdf2image import convert_from_path
import numpy as np
import csv
import glob
from nltk.tokenize import sent_tokenize as splitToSentences
if not(sys.platform in ['linux', 'posix']):
	pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# change to your tesseract installation path
baseDir = './database/'
outDirectory = baseDir + 'output/'
slidesDir = baseDir + 'slides/'
extractedDirectory = baseDir + 'extracted/'
selectedDir = ''

def getPNGFileNames(dirName):
    f = []
    for filename in os.listdir('./'+dirName+'/'):
        if filename.endswith('.png'):
            f.append(filename)
            #print(filename)
    f.sort(key=str.lower)
    return f

def combineScrapes():
    with open("combined.txt", "wb") as outfile:
        for f in glob.glob('./extracted/*'):
            with open(f, "rb") as infile:
                outfile.write(infile.read())


def scrape():
    fileNames = getPNGFileNames(outDirectory + selectedDir+ '/')
    bar =  ChargingBar('Reading Files :  ', max=len(fileNames))
    i=0
    for file in fileNames:
        i+=1
        fPath = extractedDirectory+selectedDir+ '/'+getFileName(file[:-4]) +'.txt'
        if os.path.exists(fPath):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w'        
        txtract = pytesseract.image_to_string(Image.open(outDirectory+selectedDir+ '/'+file), "eng")  
        t = txtract 
        if len(t.strip())>0: 
            f = open(fPath, append_write)
            f.write(txtract)
            f.close()
        bar.next()
    bar.finish()

  

def getDocName(strx):
    a = strx.split("-") 
    return a[0]


def getFileName(strx, style=False):
    a = strx.split("\\")    
    if style:
        return a[1]
    else:
        a = a[0].split("-")    
        return ('-'.join(a[:len(a)-2]))

def saveFilenames(fNames):   
    with open(outDirectory + selectedDir+"/extracted.csv", 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(fNames)

def createdDBDirs(dirName):
    if not(os.path.isdir(extractedDirectory+dirName+'/')):
        os.makedirs(extractedDirectory+dirName)
    if not(os.path.isdir(outDirectory+dirName+'/')):
        os.makedirs(outDirectory+dirName)     

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
            createdDBDirs(dirName)
            return str(dataBaseDirectory + dirName+'/*')
            break;
        else:
            print("Please select from one of the above listed folders")   
    
def getOutputFiles():
    f = []
    for filename in os.listdir(outDirectory):
        f.append(filename)
    f.sort(key=str.lower)
    return f         
    
def getPNGFileNames(dirName):
    f = []
    for filename in os.listdir(dirName):
        if filename.endswith('.png'):
            f.append(filename)
            #print(filename)
    f.sort(key=str.lower)
    return f
  

def saveImagesDict(images, fName):
    if len(images)<1:
        return None
    i = 0    
    for key in images:
        i+=1
        nameStr = outDirectory + selectedDir +'/' +fName+ '-' + str(i) +'.png'
        cv2.imwrite(nameStr, images[key])
 

def createGroups(img, fIDStr,iterCount = 1): 
    # iterCount was chosen by trial-and-error
    '''
    this function draws a bounding box around the identified "chunk" of text.
    each pass from the loop 'enhances' the feature as there is now a box drawn around it. 
    finally, when the loop ends, the same chunks are selected from of the original image. 
    '''
    
    imOut = img.copy()
    imCopy = img.copy()
    croppedImgs = {}

    for I in range(0, iterCount): 
        gray = imCopy.copy()
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        im2 = imCopy.copy()
        counter = 0
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = im2[y:y + h, x:x + w]      
            nStr = str(x) +'_'+str(y)+'-'+str(x + w)+'_'+str(y + h)                   
            counter+=1           
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if I==iterCount-1:
                imCropped = imOut[y:y + h, x:x+w] 
                croppedImgs[y] = imCropped
        imCopy = im2.copy() 
    
    #croppedImgs
    saveImagesDict(croppedImgs, fIDStr)
    return imOut

def loadPDF():
    pages = convert_from_path('./input/'+'test.pdf', 500)
    c = 0
    for p in pages:
        if c>0:
            p.save(str(c)+'.png', 'PNG')
        c+=1        

def getSnips():
    fileNames = getPNGFileNames(slidesDir + selectedDir)
    fCounter = 0
    if (os.path.exists(slidesDir + outDirectory+"/extracted.csv")):
        with open(slidesDir + outDirectory+"/extracted.csv", 'r', newline='') as file:
            myreader = csv.reader(file, delimiter=',')
            for rows in myreader:
                try:
                    t = ("".join(rows))
                    fileNames.remove(t)
                except ValueError:
                    pass  # do nothing!

    bar =  ChargingBar('Processing :  ', max=len(fileNames))    
    for fileName in fileNames:
        #print(slidesDir +selectedDir+fileName)
        fCounter += 1
        img = cv2.imread( slidesDir +selectedDir+'/'+fileName, 0)  # 0 converts to grayscale   
        im2 = createGroups(img, fileName[:-4])  
        bar.next()         
    bar.finish()
    
def extractorMain(dirName):
    chooseDir(dirName)
    getSnips()
    saveFilenames(getPNGFileNames(dirName+selectedDir))

#scrape()
def textractorMain():
    #chooseDir(outDirectory)
    scrape()

def runSuperMode():
    rs=False
    print('Run super mode? (completely automated)')
    print("only do this if you're sure of the database structure.")
    answer = input("Y/N : ")
    rs = (answer.upper() =="Y" )
    if rs:
        folders=[]
        directory_contents = os.listdir(slidesDir)
        for item in directory_contents:
            if os.path.isdir(slidesDir + item):
                folders.append(str(item)) 
        
        global selectedDir
        for f in folders:
            selectedDir = f
            print("Current Dir : ", f)
            createdDBDirs(f)
            getSnips()
            saveFilenames(getPNGFileNames(slidesDir+selectedDir))
            textractorMain()
            
def buildMain():
    runSuperMode()
    extractorMain(slidesDir)
    textractorMain()

buildMain()

