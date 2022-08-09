import os
import shutil
from_dir='/Users/mkonatham/Downloads'
to_dir='/Users/mkonatham/Desktop/AAEesha/Projects/Project 102/Document_Files'
list_of_files=os.listdir(from_dir)
list1=['.txt','.doc','.docx','.pdf']
print(list_of_files)

for file_name in list_of_files:
    root,extention=os.path.splitext(file_name)
    print(root)
    if(extention==""):
        print("No extention for this file")
    if(extention==list1):
        print(extention)
        print("Extention is on list")
    else: 
        print(extention)

path1=from_dir+'/'+file_name
path2=to_dir + '/' + "Document_Files"
path3=to_dir + '/' + "Document_Files" + '/' + file_name
if os.path.exists(path2):
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)
else:
    os.makedirs(path2)
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)
