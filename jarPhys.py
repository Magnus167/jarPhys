"""Unified jarPhys OCR + search pipeline in a single script."""

import glob
import json
import os
import sys
from typing import Any, Dict, List, Optional, Sequence

import cv2
import numpy as np
import pdf2image
import pytesseract
from fuzzywuzzy import fuzz
from joblib import Parallel, delayed
from tqdm import tqdm


# OCR / extraction helpers
def get_files(path: str, ext: str = "pdf") -> List[str]:
    rChar = "/" if sys.platform == "posix" else "\\"
    return [f.split(rChar)[-1] for f in glob.glob(path + "/*." + ext.lower())]


def pdf_to_imagesNpArr(pdf_path: str) -> List[np.ndarray]:
    pages = pdf2image.convert_from_path(pdf_path, dpi=250, fmt="png")
    return [np.array(pg) for pg in pages]


def get_cropped_images(img: np.ndarray, iterCount: int = 2) -> Dict[int, np.ndarray]:
    """
    Draw bounding boxes around text-like regions and return cropped images keyed
    by reading order (top-to-bottom, left-to-right).
    """

    def insert_coords(cList: List[List[int]], coord: List[int]) -> List[List[int]]:
        cList.append(coord)
        sorted(cList, key=lambda x: [x[0], x[1]])
        return cList

    def coord_to_str(coord: List[int]) -> str:
        return ",".join([str(c) for c in coord])

    imOut = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imCopy = imOut.copy()
    croppedImgs: Dict[str, np.ndarray] = {}
    coords_list: List[List[int]] = []
    gray = imCopy.copy()
    _, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contours, hierarchy = cv2.findContours(
        dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    im2 = imCopy.copy()
    coords_list = []
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        imCropped = imOut[y : y + h, x : x + w]
        coords_list = insert_coords(coords_list, [y, x])
        croppedImgs[coord_to_str([y, x])] = imCropped

    imCopy = im2.copy()
    sorted_cropped_images: Dict[int, np.ndarray] = {}
    for i, c in enumerate(coords_list):
        sorted_cropped_images[i] = croppedImgs[coord_to_str(c)]

    return sorted_cropped_images


def run_ocr(
    cropped_images_dict: Dict[str, np.ndarray], show_progress: bool
) -> List[str]:
    iterator = (
        tqdm(cropped_images_dict.keys()) if show_progress else cropped_images_dict.keys()
    )
    txtractArr = Parallel(n_jobs=-1)(
        delayed(pytesseract.image_to_string)(cropped_images_dict[file], "eng")
        for file in iterator
    )
    txtractArr = [t for t in txtractArr if len(t.strip()) > 0]
    return txtractArr[::-1]


def get_files_hash(filename: str) -> str:
    import hashlib

    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        return str(sha256_hash.hexdigest())


def save_jsonl(
    filename: str,
    textArr: Sequence[Sequence[str]],
    single_db: bool = True,
    scan_type: str = "pytesseract",
) -> bool:
    default_dbFile_name = "jarPhysDB.jsonl"
    try:
        fName = (
            "/".join(filename.split("/")[:-1]) + "/" + default_dbFile_name
            if single_db
            else (filename[:-4] + ".jsonl")
        )
        fileHash = get_files_hash(filename)
        option = "a" if os.path.exists(fName) else "w"
        with open(fName, option, encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "filename": filename,
                        "filehash": fileHash,
                        "scanType": scan_type,
                        "pages": textArr,
                    }
                )
                + "\n"
            )
    except Exception as e:
        print(e)
        print("Error saving jsonl file")
        return False
    return True


def create_db(
    folderName: Optional[str] = None,
    filenames: Optional[Sequence[str]] = None,
    single_db: bool = True,
) -> bool:
    files = get_files("./" + folderName + "/") if filenames is None else filenames
    for file in tqdm(files):
        imagesNp = pdf_to_imagesNpArr("./" + folderName + "/" + file)
        cropped_images_dicts = [get_cropped_images(img) for img in imagesNp]
        textArrs = Parallel(n_jobs=4)(
            delayed(run_ocr)(cropped_images_dict, show_progress=False)
            for cropped_images_dict in tqdm(cropped_images_dicts)
        )
        save_jsonl(
            "./" + folderName + "/" + file,
            textArrs,
            single_db=single_db,
            scan_type="pytesseract",
        )
    return True


def get_all_indexed_files(folderName: str) -> List[str]:
    db_files = get_files("./" + folderName + "/", "jsonl")
    scanEntries = []
    for db_file in db_files:
        with open("./" + folderName + "/" + db_file, "r", encoding="utf-8") as f:
            for line in f:
                d = json.loads(line)
                scanEntries.append(d["filehash"])
    return list(set(scanEntries))


def extractTextMain(folderName: Optional[str] = None) -> None:
    if folderName is None:
        folderName = "./files"
    pdfsinFolder = get_files(folderName)
    fHashes = [get_files_hash(folderName + "/" + f) for f in pdfsinFolder]
    notScanned = [
        pdfsinFolder[i]
        for i, f in enumerate(fHashes)
        if f not in get_all_indexed_files(folderName)
    ]
    if len(notScanned) == 0:
        print("All files are already scanned")
        return
    create_db(folderName, notScanned, single_db=True)


# Search helpers
def load_jsonls(path: str) -> List[Dict[str, Any]]:
    """
    Paired to save_jsonl.
    Example line in jsonl:
    {'filename': filename, 'filehash': fileHash, 'scanType': scan_type, 'pages': textArr}
    """
    jsonls = []
    for file in tqdm(get_files(path, "jsonl")):
        with open(path + "/" + file, "r") as f:
            for line in f:
                jsonls.append(json.loads(line))
    return jsonls


def jsonsl_to_dbArr(jsonls: Sequence[Dict[str, Any]]) -> List[List[Any]]:
    """
    Convert saved jsonl entries into a flat db array:
    [score_placeholder, filename, page_index, text]
    """
    dbArr = [
        [0, jsonl["filename"], i, t]
        for jsonl in jsonls
        for i, t in enumerate(jsonl["pages"])
    ]
    return dbArr


def get_file_names_from_jsonls(jsonls: Sequence[Dict[str, Any]]) -> List[str]:
    return list(set([j["filename"] for j in jsonls]))


def jarSearch(query: str, dbArr: List[List[Any]], n_jobs: int = -1) -> List[List[Any]]:
    results = dbArr.copy()
    strings_for_search = [r[3] for r in results]
    search_res = Parallel(n_jobs=n_jobs)(
        delayed(fuzz.token_set_ratio)(query, s) for s in tqdm(strings_for_search)
    )
    for i, r in enumerate(results):
        r[0] = search_res[i]
    results = sorted(results, key=lambda x: x[0], reverse=True)
    return results


def qsort(inlist: List[List[Any]], rCol: int = 0) -> List[List[Any]]:
    if len(inlist) <= 1:
        return inlist
    else:
        pivot = inlist[0]
        less = qsort([i for i in inlist[1:] if i[rCol] < pivot[rCol]])
        greater = qsort([i for i in inlist[1:] if i[rCol] >= pivot[rCol]])
        return greater + [pivot] + less


def searcherMain(folderName: Optional[str] = None) -> None:
    if folderName is None:
        folderName = "./files/"
    loaded_jsonls = load_jsonls(folderName)
    dbArr = jsonsl_to_dbArr(loaded_jsonls)

    print("Loaded Databases : ")
    print("\t".join([k.split("/")[-1] for k in get_files(folderName, "jsonl")]))
    print("Loaded Files : ")
    print(
        "\t".join([k.split("/")[-1] for k in get_file_names_from_jsonls(loaded_jsonls)])
    )
    while True:
        query = input("Enter Query: ")
        results = jarSearch(query, dbArr, n_jobs=-1)
        results = qsort(inlist=results, rCol=0)
        print("\nResults: ")
        for r in results:
            print(r[1].split("/")[-1], "\t pg: ", r[2] + 1, "\t", r[0], "%")


def jarPhysMain() -> bool:
    folderName = "./files"
    extractTextMain(folderName)
    searcherMain(folderName)
    return True


if __name__ == "__main__":
    jarPhysMain()
