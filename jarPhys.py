# %%

import sys, os, glob, math, csv, json, itertools, pdf2image, pytesseract, cv2
from tqdm import tqdm
from joblib import Parallel, delayed
from skimage.metrics import structural_similarity as ssim
import numpy as np
from nltk.tokenize import sent_tokenize as splitToSentences
from fuzzywuzzy import fuzz, process

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



def run_ocr(cropped_images_dict, show_progress):
    from joblib import Parallel, delayed

    if show_progress:
        txtractArr = Parallel(n_jobs=-1)(delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng") 
                                                                                for file in tqdm()(cropped_images_dict.keys()))
    else:
        txtractArr = Parallel(n_jobs=-1)(delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng") 
                                                                                for file in cropped_images_dict.keys())
    
    txtractArr = [t for t in txtractArr if len(t.strip())>0]


    return txtractArr[::-1]



# %%

def get_files_hash(filename):
    import hashlib
 
    # filename = input("Enter the input file name: ")
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        # print(sha256_hash.hexdigest())
        return str(sha256_hash.hexdigest())


def save_jsonl(filename, textArr,  single_db=True, scan_type='pytesseract'):
    default_dbFile_name = 'jarPhysDB.jsonl'
    try:
        fName = '/'.join(filename.split('/')[:-1]) + '/' + default_dbFile_name if single_db else (filename[:-4] + '.jsonl')
        fileHash = get_files_hash(filename)
        option = 'a' if os.path.exists(fName) else 'w'
        with open(fName, option, encoding='utf-8') as f:
            f.write(json.dumps({'filename' : filename, 'filehash': fileHash, 'scanType' : scan_type, 'pages' : textArr}) + '\n')
    except Exception as e:
        print(e)
        print('Error saving jsonl file')
        return False
    return True


def create_db(folderName=None, filenames=None,single_db=True):
    files = get_files('./'+folderName + '/') if filenames is None else filenames
    for file in tqdm(files):
        imagesNp = pdf_to_imagesNpArr('./' + folderName + '/' + file)
        cropped_images_dicts = [get_cropped_images(img) for img in imagesNp]
        textArrs  = Parallel(n_jobs=4)(delayed(run_ocr)(cropped_images_dict, show_progress=False) for cropped_images_dict in tqdm(cropped_images_dicts))
        # in the future, where different types of scans are done, the scan function also returns the scan type.
        save_jsonl('./' + folderName + '/' + file, textArrs, single_db=single_db, scan_type='pytesseract')
    return True

def get_all_indexed_files(folderName):
    db_files = get_files('./'+folderName + '/', 'jsonl')
    scanEntries = []
    for db_file in db_files:
        with open('./'+folderName + '/' + db_file, 'r', encoding='utf-8') as f:
            for line in f:
                d = json.loads(line)
                scanEntries.append(d['filehash'])
    return list(set(scanEntries))

def extractTextMain(folderName=None):
    
    if folderName is None:
        folderName = './files'
    # available_scan_types = ['pytesseract']
    pdfsinFolder = get_files(folderName)
    fHashes = [get_files_hash(folderName + '/' + f) for f in pdfsinFolder]
    # possible_combos = list(itertools.product(fHashes, available_scan_types))
    notScanned = [pdfsinFolder[i] for i, f in enumerate(fHashes) if f not in get_all_indexed_files(folderName)]
    if len(notScanned) == 0:
        print('All files are already scanned')
        return
    create_db(folderName, notScanned, single_db=True)
    
# %%


# %%



def get_files(path, ext='pdf'):
    rChar = '/' if sys.platform == 'posix' else '\\'
    return [f.split(rChar)[-1] for f in glob.glob(path + '/*.' + ext.lower())]

def load_jsonls(path):
    ''' paired to extract_text.py/save_jsonl
        example line in jsonl:
        {'filename' : filename, 'filehash': fileHash, 'scanType' : scan_type, 'pages' : textArr}
    '''
    jsonls = []
    for file in tqdm(get_files(path, 'jsonl')):
        with open(path + '/' + file, 'r') as f:
            for line in f:
                jsonls.append(json.loads(line))
    return jsonls


# %%

# def jsonls_to_dbDict(jsonls):
#     filenames       = [j["filename"] for j in jsonls]
#     dbDict          = dict([(f, {}) for f in list(set(filenames))])
#     for jsonl in jsonls:
#         dbDict[jsonl["filename"]][jsonl["pageNum"]] = jsonl["text"]
#     return dbDict

# def dbDict_to_dbArr(dbDict):
#     dbArr = [[filename, pageNum, dbDict[filename][pageNum], 0] for filename in dbDict for pageNum in dbDict[filename]]
#     return dbArr


# %%

def jsonsl_to_dbArr(jsonls):
    ''' paired to extract_text.py/save_jsonl
        example line in jsonl:
        {'filename' : filename, 'filehash': fileHash, 'scanType' : scan_type, 'pages' : textArr}
    '''
    dbArr = [[0, jsonl["filename"], i, t] for jsonl in jsonls for i, t in enumerate(jsonl["pages"])]
    return dbArr

def get_file_names_from_jsonls(jsonls):
    return list(set([j["filename"] for j in jsonls]))

# %%
            
def jarSearch(query, dbArr, n_jobs=-1):
    results = dbArr.copy()
    strings_for_search = [r[3] for r in results]
    search_res = Parallel(n_jobs=n_jobs)(delayed(fuzz.token_set_ratio)(query, s) for s in tqdm(strings_for_search))
    for i, r in enumerate(results):
        r[0] = search_res[i]
    results = sorted(results, key=lambda x: x[0], reverse=True)
    return results



def qsort(inlist, rCol=0):

    if len(inlist) <= 1:
        return inlist
    else:
        pivot = inlist[0]
        less = qsort([i for i in inlist[1:] if i[rCol] < pivot[rCol]])
        greater = qsort([i for i in inlist[1:] if i[rCol] >= pivot[rCol]])
        # return less + [pivot] + greater
        return greater + [pivot] + less

# %%
def searcherMain(folderName=None):
    # dbDict = jsonls_to_dbDict(load_jsonls('./files/'))
    if folderName is None:
        folderName = './files/'
    loaded_jsonls = load_jsonls(folderName)
    dbArr = jsonsl_to_dbArr(loaded_jsonls)

    print("Loaded Databases : ")
    print('\t'.join([k.split('/')[-1] for k in get_files(folderName, 'jsonl')]))
    print("Loaded Files : ")
    print('\t'.join([k.split('/')[-1] for k in get_file_names_from_jsonls(loaded_jsonls)]))
    while True:
        query = input("Enter Query: ")
        results = jarSearch(query, dbArr, n_jobs=-1)
        results = qsort(inlist=results, rCol=0)
        print("\nResults: ")
        for r in results:
            print(r[1].split('/')[-1], '\t pg: ', r[2]+1, '\t', r[0], '%')


def jarPhysMain():
    folderName = './files'
    extractTextMain(folderName)
    searcherMain(folderName)
    return True

if __name__ == '__main__':
    jarPhysMain()