import json 

file_path = "file_handeling\\writing_files\\output_dicts.json"

with open(file_path , "r") as file : 
    reader = json.load(file)
    print(reader["name"])  # to access a perticular value

    

