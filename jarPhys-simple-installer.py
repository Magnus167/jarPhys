import subprocess
import sys
import os
import shutil
import time

subprocess.check_call(' '.join(["python3 -m pip install requests"]))
subprocess.check_call(' '.join("python3 -m pip install zipfile38"]))

import requests 
from zipfile38 import ZipFile

def download_zip(url, fileName='./main.zip', chunk_size=128):
    r = requests.get(url, stream=True)
    with open(fileName, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    
    with ZipFile(fileName, 'r') as zipObj:
        zipObj.extractall()
    
    os.rename('./jarPhys-main','./jarPhys')  
    os.remove(fileName)

download_zip('https://codeload.github.com/Magnus167/jarPhys/zip/refs/heads/main')
print('...')
time.sleep(3)
time
selfDir = os.getcwd()
os.chdir('./jarPhys')
print('...')
time.sleep(3)
from jarPhys.installer import *
installerX()
os.chdir(selfDir)
os.remove('jarPhys-simple-installer.py')
