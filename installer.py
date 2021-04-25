import subprocess
import sys
import os
import shutil
def installerX():
    gDriveLinks = {}
    gDriveLinks['slides'] =     '1LpSFZ502WHYD0bm7ALeClbIb4mSlfBNC'
    gDriveLinks['output'] =     '1SbYh2A68PgXHgfmxdj7_0Z8tjpm2aF721'
    gDriveLinks['extracted'] =  '1RXCyroG514CBVJdTo2GaMOStgX8fSkOK'
    # slides.zip    https://drive.google.com/file/d/1LpSFZ502WHYD0bm7ALeClbIb4mSlfBNC/view?usp=sharing
    # output.zip    https://drive.google.com/file/d/1SbYh2A68PgXHgfmxdj7_0Z8tjpm2aF72/view?usp=sharing
    # extracted.zip https://drive.google.com/file/d/1RXCyroG514CBVJdTo2GaMOStgX8fSkOK/view?usp=sharing
    # complete_repo https://drive.google.com/drive/folders/18VgVaxoDj531Imugoc_VvvTUzCvTQdZ9?usp=sharing

    subprocess.check_call("python3 -m pip install -r requirements.txt")
    subprocess.check_call("python3 -m nltk.downloader all")
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
