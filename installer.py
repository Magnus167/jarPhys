import subprocess
import sys
subprocess.check_call(' '.join([sys.executable, "-m pip install -r requirements.txt"]))
subprocess.check_call(' '.join([sys.executable, "-m nltk.downloader all"]))


from google_drive_downloader import GoogleDriveDownloader as gdd
# #https://drive.google.com/file/d/13Ac06UG612NMIP771zqwspPkCf-Hj8Vk/view?usp=sharing
gdd.download_file_from_google_drive(file_id='13Ac06UG612NMIP771zqwspPkCf-Hj8Vk' , dest_path='./database.zip', unzip=False, showsize=True)

import zipfile
with zipfile.ZipFile('./database.zip', 'r') as zip_ref:
    zip_ref.extractall('./database')