# input() A function that prompts the user to enter data
#         Returns the entire data as a string

name = input("please enter your name :")
age = int(input("Enter your age :"))
# we taking one extra line of code 
#age = int(age)
age = age + 1  
print(f"Hello {name}! Nice to meet you!")
print(f"You are now {age} years old!!!!")