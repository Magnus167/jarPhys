import numpy as np
import PIL.Image as Image
import pdf2image
import sys, os, glob, math
from tqdm import tqdm
from joblib import Parallel, delayed


def get_files(path, ext='pdf'):
    rChar = '/' if sys.platform == 'posix' else '\\'
    return [f.split(rChar)[-1] for f in glob.glob(path + '/*.' + ext.lower())]

def pdf_to_images(pdf_path):
    pages = pdf2image.convert_from_path(pdf_path, dpi=450, fmt='png')
    # for pg in range(len(pages)):
    #     pages[pg].save('out_imgs/' + str(pg) + '.png')
    return [pg for pg in pages]