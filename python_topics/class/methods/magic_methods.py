# Magic Methods = Dunder methods (double underscore) __init__ , __str__ ,   __eq__
#          They are automatically called by many of python's built in operations
#           They allow developers to define or customize the behavior of objects. 

class Book : 
    def __init__(self,title,author,num_pages) : 
        self.title = title 
        self.author = author
        self.num_pages = num_pages

    def __str__(self) : 
        return f"{self.book} by {self.author}"
    
    def __eq__(self , other) : 
        return self.title == other.title and self.author == other.author

    def __gt__(self , other) : 
        return self.num_pages > other.num_pages
    
    def __lt__(self , other) : 
        return self.num_pages < other.num_pages

    def __contains__(self, item):
        return item in self.author or item in self.title

    def __getitem__(self, key):
        if key == "Title" : 
            return self.title
        elif key == "Author" : 
            return self.authot 
        elif key == "num_pages" : 
            return self.num_pages
        else :
            return f"{key} Not found"



book1 = Book("The Alcemist" , "Paulo Coelho" , 100)
book2 = Book("Paradise Lost" , "John Milton" , 300)
book3 = Book("Odyssey" , "Homer" , 500)
book4 = Book("The Alcemist" , "Paulo Coelho" , 100) #just to try __eq__
print(book1 == book4) # testing __eq__
print(book1 > book2) #testing __gt__
print(book1 < book2) #testing __lt__
print("Paulo" in book1 ) # testing __contains__
print(book1['num_pages']) # testing _getitem__
