employee = ["Mr. Krabs" , "Spongebob" , "Patrick" , "Squidward"]
file_path = "file_handeling\\writing_files\\output_list.txt"
with open(file_path , "a" ) as file : 
    for people in employee : 
        file.write(people + "\n")

