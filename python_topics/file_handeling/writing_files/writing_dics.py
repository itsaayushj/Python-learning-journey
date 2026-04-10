# json = JavaScript Object Notation
import json # to use the dup method
employee = {
    "name" : "Naruto" ,
    "age" : 30 , 
    "role" : "hokage"
}
file_path = "file_handeling\\writing_files\\output_dicts.json"

with open(file_path , "w") as file : 
    json.dump(employee , file , indent= 4) # indent is used for formatting it nicely
# json.dump needs a location to write so we passed file again 


