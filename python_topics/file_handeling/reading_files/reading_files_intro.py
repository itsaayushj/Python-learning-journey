# Python reading files (.txt , .json , .csv)

file_path = "file_handeling\\writing_files\\output_writing_fles.txt"
try : 
    with open(file_path , "r") as file : 
        content = file.read()
        print(content)
except FileNotFoundError as f :
    print(f)

