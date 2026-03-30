# list comprehension = A concise way to create lists in python 
#                         compact and easier to read than traditional loops
#                         [expression for value in iterable if condition]

# double = [x *2 for x in range(1,11)]
double = []
[double.append(x*2) for x in range(1,11)]
print(double)
letters = ["Aa" , "Bb" , "Cc" , "Dd"]
letters_chars = [each_letter[0] for each_letter in letters]
print(letters_chars)

nums = [0 , -2 , -49 , 84 , 82 , -74 , -38 , 72 , 31]
positive_nums = [num for num in nums if num >= 0]
print(positive_nums)
negative_nums = [num for num in nums if num <0 ]
print(negative_nums)
even_nums = [num for num in nums if num % 2 == 0 ]
print(even_nums)
odd_nums = [num for num in nums if num %2 != 0]
print(odd_nums)


