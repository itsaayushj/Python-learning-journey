import csv
file_path = "file_handeling\\writing_files\\output_csv.csv"

with open(file_path , "r") as file  : 
    reader = csv.reader(file) 
    print(reader) # this will return memory address we have to read it line by line

    for line in reader : 
        print(line[0])
        



