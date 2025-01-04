# first import os module
import os
# specify the directory ypu want to list
directory_path ="/users"
# list all files and directories in the specified path
content = os.listdir(directory_path)
# print all the files and directories
for item in content:
    print(item)