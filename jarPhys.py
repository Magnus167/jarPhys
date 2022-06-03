# %%
from PIL import Image
import numpy as np
import cv2
import pytesseract
from progress.bar import ChargingBar
from skimage.metrics import structural_similarity as ssim
import imutils
from pdf2image import convert_from_path
from nltk.tokenize import sent_tokenize as splitToSentences
import sys
import PIL.Image as Image
import pdf2image
import sys, os, glob, math, csv, json
from tqdm import tqdm
from joblib import Parallel, delayed


# %%



def get_files(path, ext='pdf'):
    rChar = '/' if sys.platform == 'posix' else '\\'
    return [f.split(rChar)[-1] for f in glob.glob(path + '/*.' + ext.lower())]

def pdf_to_imagesNpArr(pdf_path):
    pages = pdf2image.convert_from_path(pdf_path, dpi=250, fmt='png')
    return [np.array(pg) for pg in pages]


def get_cropped_images(img, iterCount=2):
    '''
    this function draws a bounding box around the identified "chunk" of text.
    each pass from the loop 'enhances' the feature as there is now a box drawn around it. 
    finally, when the loop ends, the same chunks are selected from of the original image. 
    not fixed. change to return a sorted dict of images
    '''
    def insert_coords(cList, coord):
        cList.append(coord)
        sorted(cList, key=lambda x: [x[0], x[1]])
        return cList
    def coord_to_str(coord):
        return ','.join([str(c) for c in coord])
    
    def str_to_coord(strCoord):
        return [int(c) for c in strCoord.split(',')]
        
    imOut = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imCopy = imOut.copy()
    croppedImgs = {}
    coords_list = []
# for I in range(0, iterCount): 
    gray = imCopy.copy()
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = imCopy.copy()
    counter = 0
    coords_list = []
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = im2[y:y + h, x:x + w]                     
        counter+=1           
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        imCropped = imOut[y:y + h, x:x+w]
        coords_list = insert_coords(coords_list, [y, x])
        croppedImgs[coord_to_str([y, x])] = imCropped

    imCopy = im2.copy() 
    sorted_cropped_images = {}
    for i, c in enumerate(coords_list):
        sorted_cropped_images[i] = croppedImgs[coord_to_str(c)]


    return sorted_cropped_images



def run_ocr(cropped_images_dict, show_progress=True):
    from joblib import Parallel, delayed

    if show_progress:
        txtractArr = Parallel(n_jobs=-1)(delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng") 
                                                                                for file in tqdm(cropped_images_dict.keys()))
    else:
        txtractArr = Parallel(n_jobs=-1)(delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng") 
                                                                                for file in cropped_images_dict.keys())
    
    txtractArr = [t for t in txtractArr if len(t.strip())>0]


    return txtractArr[::-1]



# %%


def save_jsonl(filename, textArr):
    with open(filename[:-4] + '.jsonl', 'w', encoding='utf-8') as f:
        for i, t in enumerate(textArr):
            f.write(json.dumps({'filename' : filename, 'pageNum' : i, 'text' : t}) + '\n')
    return True


def create_db(folderName):
    files = get_files('./' + folderName + '/')
    built_files = get_files('./' + folderName + '/', 'jsonl')
    files = [f for f in files if f[:-4] + '.jsonl' not in built_files]
    for file in tqdm(files):
        imagesNp = pdf_to_imagesNpArr('./' + folderName + '/' + file)
        cropped_images_dicts = [get_cropped_images(img) for img in imagesNp]
        textArrs  = Parallel(n_jobs=-1)(delayed(run_ocr)(cropped_images_dict, show_progress=True) for cropped_images_dict in tqdm(cropped_images_dicts))
        save_jsonl('./' + folderName + '/' + file, textArrs)
    return True
    

# %%


# %%
from fuzzywuzzy import fuzz, process
from tqdm import tqdm
from joblib import Parallel, delayed
import sys, os, glob, json

def get_files(path, ext='pdf'):
    rChar = '/' if sys.platform == 'posix' else '\\'
    return [f.split(rChar)[-1] for f in glob.glob(path + '/*.' + ext.lower())]

def load_jsonls(path):
    jsonls = []
    for file in tqdm(get_files(path, 'jsonl')):
        with open(path + '/' + file, 'r') as f:
            for line in f:
                jsonls.append(json.loads(line))
    return jsonls


# %%

def jsonls_to_dbDict(jsonls):
    filenames       = [j["filename"] for j in jsonls]
    dbDict          = dict([(f, {}) for f in list(set(filenames))])
    for jsonl in jsonls:
        dbDict[jsonl["filename"]][jsonl["pageNum"]] = jsonl["text"]
    return dbDict

def dbDict_to_dbArr(dbDict):
    dbArr = [[filename, pageNum, dbDict[filename][pageNum], 0] for filename in dbDict for pageNum in dbDict[filename]]
    return dbArr

            
def search(query, dbDict, dbArr=None):
    if dbArr is None:
        dbArr = dbDict_to_dbArr(dbDict)
    results = dbArr
    search_res = Parallel(n_jobs=-1)(delayed(fuzz.token_set_ratio)(query, dbArr[2]) for dbArr in tqdm(results))
    for i, r in enumerate(results):
        r[3] = search_res[i]
    results = sorted(results, key=lambda x: x[3], reverse=True)
    return results


    



# %%
def main():
    
    create_db('files')
    dbDict = jsonls_to_dbDict(load_jsonls('./files/'))
    dbArr = dbDict_to_dbArr(dbDict)
    print("Loaded Files : ")
    print('\t'.join([k.split('/')[-1] for k in dbDict.keys()]))
    while True:
        query = input("Enter Query: ")
        results = search(query, dbDict, dbArr)
        for r in results:
            print(r[0].split('/')[-1], '\t\t pg: ', r[1]+1, '\t\t', r[3], '%')



if __name__ == '__main__':
    main()