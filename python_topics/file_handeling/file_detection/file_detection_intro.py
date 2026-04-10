#  Python file detection

import os # os means operating system 

# while giving file path \ can cause error. we can replace it with \\ or / 
file_path = "file_detection/test.txt" #relative file paths or absolute file path 

if os.path.exists(file_path) : 
    print(f"The path '{file_path}' does exists!")
    if os.path.isdir(file_path) : 
        print("It is a folder!")
    elif os.path.isfile(file_path) : 
        print("It is a file!")
else : 
    print(f"'{file_path}' does not exists!")

print(os.getcwd()) # to get the current working directory (where the program is running from)
print(__file__) # full path of the current .py file 
base_dir = os.path.dirname(__file__) #gives the parent folder
print(base_dir)
os.path.exists(os.path.join(base_dir , 'test.txt')) # asks it to go into base_dir and search for text.txt // os.path.join joins both.
# NOTE: 
# Python uses CWD (Current Working Directory)
# That means it looks for files from where the program is RUN,
# not where this .py file is.
# So "test.txt" may not work unless CWD is correct.
