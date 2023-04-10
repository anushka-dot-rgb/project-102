import os
import shutil

from_dir = "C:/Users/aishwarya/Downloads"
to_dir = "C:/Users/aishwarya/Documents"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' +  "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        #Check if Folder/Directory Path exists before moving
        #Else make a Folder/Directory then move

        if os.path.exists(path2):
            #Move from path1 ---> path3
            shutil.move(path1,path3)
            print("Moving "+file_name+"...")
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("Moving "+file_name+"...")