#  Class methods = Allow operations related to the class itself 
#                   Take (cls) as the first parameter, which represents the class itself.

class Students : 
    student_count = 0 
    total_gpa = 0
    def __init__(self , name , gpa) : 
        self.name = name 
        self.gpa = gpa
        student_count += 1 
        total_gpa += gpa # can also write self.gpa but this is faster and better
    
    def get_info(self) : # instance method
        return f"{self.name} - {self.gpa}"
    
    @classmethod 
    def get_totalstudents(cls) :
        return f"the total students are {cls.student_count}"

    @classmethod 
    def get_averagegpa(cls) : 
        if cls.student_count == 0 :
            return "0 , There are no students!"
        else : 
            return f"the average gpa of class is {cls.total_gpa / cls.student_count:.2f}"
    

    
