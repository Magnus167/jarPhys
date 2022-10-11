from fuzzywuzzy import fuzz, process
from tqdm import tqdm
from joblib import Parallel, delayed
import sys, os, glob, json

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
    # results = sorted(results, key=lambda x: x[0], reverse=True)
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
def searcherMain():
    # dbDict = jsonls_to_dbDict(load_jsonls('./files/'))
    folderPath = './files/'
    loaded_jsonls = load_jsonls(folderPath)
    dbArr = jsonsl_to_dbArr(loaded_jsonls)

    print("Loaded Databases : ")
    print('\t'.join([k.split('/')[-1] for k in get_files(folderPath, 'jsonl')]))
    print("Loaded Files : ")
    print('\t'.join([k.split('/')[-1] for k in get_file_names_from_jsonls(loaded_jsonls)]))
    while True:
        query = input("Enter Query: ")
        results = jarSearch(query, dbArr, n_jobs=-1)
        results = qsort(inlist=results, rCol=0)
        print("\nResults: ")
        for r in results:
            print(r[1].split('/')[-1], '\t pg: ', r[2]+1, '\t', r[0], '%')


if __name__ == '__main__':
    searcherMain()