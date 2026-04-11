import csv
file_path = "file_handeling\\writing_files\\output_csv.csv"

with open(file_path , "r") as file  : 
    reader = csv.reader(file) 
    print(reader) # this will return memory address we have to read it line by line

    for line in reader : 
        print(line[0])
        
    for line in reader : #it wont run twice, we have to turn reader into list to make it run twice.It can be looped only once
        print(line)
        



