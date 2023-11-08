import os
import shutil

from_dir = 'C102_assets-main'
to_dir = 'organized_files'

files = os.listdir(from_dir)

for index in files:
    name , extension = os.path.splitext(index)
    #print(f'filename is {name}, and the extension is {extension}')
    if extension in ['.txt','.doc','.docx','.pdf']:

        path1 = from_dir + "/" + index
        path2 = to_dir + "/" + 'Document_Files'
        path3 = to_dir + "/" + 'Document_Files' + "/" + index

        if os.path.exists(path2):
            print("folder exists")
            shutil.move(path1,path3)
            print("file moved")
        else :
            print("folder doesnt exist")
            os.mkdir(path2)
            print("folder created")
            shutil.move(path1,path3)
            print("file moved")
