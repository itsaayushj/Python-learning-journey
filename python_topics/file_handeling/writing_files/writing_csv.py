# CSV = Comma-Separated Values
import csv
employee = [["name" , "age" , "role"] , ["Spongebob" , 30 , "cook"] , ["patrick" , 37 , "unemployed"] , ["Mr Krabs" , 50 , "Manager"]]

file_path = "file_handeling\\writing_files\\output_csv.csv"

with open(file_path , "w" , newline="\n") as file : 
    writer = csv.writer(file) # # csv.writer wraps the file and handles proper CSV formatting (commas, quotes, etc.)
    for row in employee : 
        writer.writerow(row)

