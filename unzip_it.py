from zipfile import ZipFile
import os

path = "D:\\GD\\Gradients\\zipp\\" # Provide the full directory path of the zip files
dir_list = os.listdir(path) # List all the zip files in the directory

for zip_file in dir_list:
    with ZipFile(path+zip_file, 'r') as zipObj:
        listOfFileNames = zipObj.namelist() # Get all the file names in the zip file
        
        for fileName in listOfFileNames:
            if fileName.endswith('.eps'):  # Change the extension as per your requirement
                zipObj.extract(fileName, 'folder_name')   # Replace "folder_name" with the name of the folder you want to extract the files to

print('All the eps files are extracted')