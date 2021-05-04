import subprocess
import sys
import os
import shutil
import urllib
def installerX():
    def updateDatabase(devX=False):  
        url = "https://raw.githubusercontent.com/Magnus167/jarPhys/main/databaseLinks.txt"
        file = urllib.request.urlopen(url)
        fileList = []
        for line in file:
            decoded_line = line.decode("utf-8")
            fileList.append(decoded_line.split(', '))
        for fs in fileList:
                fID = fs[1].split('/')[-1].strip()   
                if not(devX):         
                    if not(fs[0]=='output.zip'):
                        downloadFile(fID, fs[0])
                else:
                    downloadFile(fID, fs[0])

    subprocess.check_call("python -m pip install -r requirements.txt", shell=True)
    subprocess.check_call("python -m nltk.downloader all", shell=True)
    from progress.bar import ChargingBar
    from zipfile38 import ZipFile

    devFiles = ["Install_Instructions.txt", "database.txt", "LICENSE.txt", "README.txt", "installer.py", "requirements.txt", "buildDatabase.py", "results.html", "jarPhys-simple-installer.py","databaseLinks.txt"]

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
    updateDatabase(devMode)
    if not(devMode):
        if os.path.isfile('README.md'):
            os.rename('README.md','README.txt')
        if os.path.isfile('LICENSE'):
            os.rename('LICENSE','LICENSE.txt')        
        os.rename('searcher.py','jarPhys-search.py')
        os.mkdir("./jarPhys-info")
        for f in devFiles:
            os.rename(f, "./jarPhys-info" + '/'+f)

    print("Install successful!")
    #print("You can now delete installer.py :D")
    print("")
    print("")
    input("press enter to close the installer. __ >")


installerX()
