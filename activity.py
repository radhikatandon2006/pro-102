import os
import shutil

from_dir = 'C102_assets-main'
to_dir = 'organized_files'

files = os.listdir(from_dir)
'''
['Badminton.gif', 'ChatBot-01.png', 'Dog-walk.gif', 'feather.jfif', 'Field-01.jpg', 'mushroom-house.jpg', 'Story Board 2-01.jpg']
'''

for index in files:
    name , extension = os.path.splitext(index)
    #print(f'filename is {name}, and the extension is {extension}')
    if extension in ['.gif','.png','.jfif','.jpg']:
        path1 = from_dir + "/" + index
        path2 = to_dir + "/" + 'image_files'
        path3 = to_dir + "/" + 'image_files' + "/" + index

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













