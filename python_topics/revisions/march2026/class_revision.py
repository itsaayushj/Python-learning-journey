# revision for basic class and method 
class student : 
    class_year = 2026  # these are class variables
    total_student = 0 
    total_subjects = 5 
    def __init__(self , name , age , total_marks) : 
        self.name = name  # these are instance variable 
        self.age = age 
        self.total_marks = total_marks
        student.total_student += 1 

    def percentage(self) : 
        self.grade = (self.total_marks / (student.total_subjects * 100))  * 100

student1 = student("spongebob" , 18 , 350 )
student2 = student("patrick" , 10 , 25)
student3 = student("Mr.krabs" , 89 , 455)
# calling the method so it can create self.grade
student1.percentage()
student2.percentage()
student3.percentage()
print(student1.name , student1.age , student.class_year , student.total_student)
print(f"{student1.name} got {student1.grade:.2f} %")
print(f"{student2.name} got {student2.grade:.2f} %")
print(f"{student3.name} got {student3.grade:.2f} %")


