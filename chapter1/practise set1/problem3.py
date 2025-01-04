# A program to print the contents of the file using the od module.
import os
directory_path ="/users"
content = os.listdir(directory_path)
for item in content:
    print(item)