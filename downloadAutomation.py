import os
import shutil
import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("File Organiser", "Process has been started", duration=10)

os.chdir('C:/Users/Dope/Desktop/DownloadAutomator')
# Files Download Path
downloadPath = "C:/Users/Dope/Downloads"

# Destination File Paths
docsPath = "D:/Downloads/Documents (.docx)"
exePath = "D:/Downloads/Executables"
pdfPath = "D:/Downloads/PDFs"
picturesPath = "D:/Downloads/Pictures"
zipPath = "D:/Downloads/Zip files"
songsPath = "D:/Downloads/MP3 files"
othersPath = "D:/Downloads/Other files"

def moveFiles():
    for file in os.scandir(downloadPath):
        fileName = file.name
        sourcePath = ('{}/{}'.format(downloadPath, fileName))
        if '.pdf' in fileName:
            destPath = ('{}/{}'.format(pdfPath, fileName))

        elif '.docx' in fileName:
            destPath = ('{}/{}'.format(docsPath, fileName))

        elif '.exe' in fileName:
            destPath = ('{}/{}'.format(exePath, fileName))

        elif ('.jpeg' in fileName) or ('.jpg' in fileName) or ('.png' in fileName):
            destPath = ('{}/{}'.format(picturesPath, fileName))

        elif '.zip' in fileName or '.rar' in fileName:
            destPath = ('{}/{}'.format(zipPath, fileName))

        elif '.mp3' in fileName:
            destPath = ('{}/{}'.format(songsPath, fileName))

        else:
            destPath = ('{}\{}'.format(othersPath, fileName))

        shutil.move(sourcePath, destPath)

while True:
    moveFiles()
    
        
    

