# Python writing files (.txt , .json , .csv)
txt_data = "I love minecraft!"
file_path = "file_handeling\\writing_files\\output_writing_files.txt"

# while using 'with' python automatically closes the file after the code block is done
with open(file_path ,"w") as file :
    # 'as f' assigns the opened file object to variable f for use inside the block
    file.write(f"{txt_data} \n")
    print(f"{file_path} was created/edited")
     # we can skip writing file= and mode= , we can use "w" to write and create if it does not already exists, "x" to create and write (does not work if file already exists) , "r" to read and "a" to append
    
