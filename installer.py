import subprocess
import sys
import os
import shutil
def installerX():
    gDriveLinks = {}
    gDriveLinks['slides'] =     '12OVU0vfi2Z6ZYY3zSOHDzb15kPH_84K8'
    gDriveLinks['output'] =     '15JNnLW6rKrFMa7EK7fc0oBnMBt1Ihpsy'
    gDriveLinks['extracted'] =  '1HibfoC1LkHEUg8a5cU-gQNZ3C3rHbajK'
    # slides.zip    https://drive.google.com/file/d/12OVU0vfi2Z6ZYY3zSOHDzb15kPH_84K8/view?usp=sharing
    # output.zip    https://drive.google.com/file/d/15JNnLW6rKrFMa7EK7fc0oBnMBt1Ihpsy/view?usp=sharing
    # extracted.zip https://drive.google.com/file/d/1HibfoC1LkHEUg8a5cU-gQNZ3C3rHbajK/view?usp=sharing
    # complete_repo https://drive.google.com/drive/folders/18VgVaxoDj531Imugoc_VvvTUzCvTQdZ9?usp=sharing

    subprocess.check_call("python -m pip install -r requirements.txt", shell=True)
    subprocess.check_call("python -m nltk.downloader all", shell=True)
    from progress.bar import ChargingBar
    from zipfile38 import ZipFile

    devFiles = ["Install_Instructions.txt", "database.txt", "LICENSE.txt", "README.txt", "installer.py", "requirements.txt", "buildDatabase.py", "results.html", "jarPhys-simple-installer.py"]

    print('..............')
    print("Do you want to enable developer mode?")
    print("(Unless you're going to be writing code for this project, say no)")
    answer = input("Y/N : ")
    devMode = (answer.upper() == 'Y')
    if devMode:
        print("Downloading developer files")
    else:    
        print("Skiping developer files")

    from google_drive_downloader import GoogleDriveDownloader as gdd
    def downloadFile(id, dest, folderX='./database/'):
        gdd.download_file_from_google_drive(file_id=id , dest_path=folderX+dest, unzip=False, showsize=True)
        print("Unzipping... [typically 5-10ish minutes]")
        with ZipFile(folderX+dest, 'r') as zipObj:
            zipObj.extractall(folderX)    
        os.remove(folderX+dest)


    os.mkdir("./database/")
    uzipFiles = []
    if devMode:
        downloadFile(gDriveLinks['extracted'], 'extracted.zip')
        downloadFile(gDriveLinks['slides'], 'slides.zip')
        downloadFile(gDriveLinks['output'], 'output.zip')
    else:
        downloadFile(gDriveLinks['extracted'], 'extracted.zip')
        downloadFile(gDriveLinks['slides'], 'slides.zip')
        if os.path.isfile('README.md'):
            os.rename('README.md','README.txt')
        if os.path.isfile('LICENSE'):
            os.rename('LICENSE','LICENSE.txt')        
        os.rename('searcher.py','jarPhys-search.py')
        os.mkdir("./jarPhys-info")
        for f in devFiles:
            os.rename(f, "./jarPhys-info" + '/'+f)
        # start for standalone installer.

    print("Install successful!")
    #print("You can now delete installer.py :D")
    print("")
    print("")
    input("press enter to close the installer. __ >")


installerX()
