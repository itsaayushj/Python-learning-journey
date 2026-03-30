#  Iterable - An object / collection that can return its element one at a time, allowing it to be iterable over in a loop

# lists[] , # tuples() , dictionaries{} , strings 

eg_string = "Bruce Wayne"
eg_tuple = (1 , 2 ,3 ,4 ,5 )
eg_list = [ 1 , 2 ,3 ,4]
eg_set = {1 ,2 ,3, 4, 5}
eg_dictionary = {"a" : 1 , "b" : 2 , "c" : 3}
for character in eg_string :
    print(character , end="")

for stuff in eg_list : 
    print(stuff , end="-")

for stuff in eg_tuple : 
    print(stuff , end="-")

for stuff in eg_set:
    print(stuff)

for key , value in eg_dictionary.items() : 
    print(f"{key} , {value}")
