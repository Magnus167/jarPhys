import subprocess
import sys
import os
import shutil
subprocess.check_call(' '.join([sys.executable, "-m pip install -r requirements.txt"]))
subprocess.check_call(' '.join([sys.executable, "-m nltk.downloader all"]))

from google_drive_downloader import GoogleDriveDownloader as gdd
# #https://drive.google.com/file/d/13Ac06UG612NMIP771zqwspPkCf-Hj8Vk/view?usp=sharing
print ("Downloading database.zip fro Google Drive. Approx. Size = 700MB")
gdd.download_file_from_google_drive(file_id='13Ac06UG612NMIP771zqwspPkCf-Hj8Vk' , dest_path='./database.zip', unzip=False, showsize=True)

import zipfile
print("Unzipping File... Please wait (this may take 2-3 minutes)")
with zipfile.ZipFile('./database.zip', 'r') as zip_ref:
    zip_ref.extractall('.')    
os.remove("database.zip")
print('..............')
print("Do you want to keep developer files?")
print("(Unless you're going to be writing code for this project, say no)")
while True:
        answer = input("Y/N : ")
        if answer.upper() == 'Y':
            print("Retaining developer files")
            break;
        else:
            print("Deleting developer files")
            os.remove("requirements.txt")
            os.remove("buildDatabase.py")
            shutil.rmtree("./database/output")
            break;

print("Install successful!")
