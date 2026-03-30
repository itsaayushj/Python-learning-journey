#  class variable = Shared among all instance of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from
#                   That class
class students : 
    class_year = 2026
    total_students = 0 
    def __init__(self , name , age ) : 
        self.name = name        # instance variables
        self.age = age          # instance variables 
        students.total_students += 1 
student1 = students("Doraemon" , 100)
student2 = students("Nobita" , 10 )
student3 = students("Sinchan" , 5 )
student4 = students("hatori" , 12)
print(student1.name , student1.age , students.class_year)
print(student2.name , student2.age , students.class_year)
print(student3.name , student3.age , students.class_year)
print(f"Total students in the class of {students.class_year} are {students.total_students}")


