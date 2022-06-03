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