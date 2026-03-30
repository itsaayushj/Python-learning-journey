# Typecastig = To convert one datatype to another
# type() str() bool() float() int()
name = "aayush"
age = 19 
is_student = True
gpa = 4.5
type(gpa) # nothing will be shown in output as we have not printed anything
print(type(gpa))
print(name)

age = str(age)
print(age)
print(type(age))

name = name +"1" 
print(name)
print(name + "1")
print(type(name))
# here age is 191 and not 20 because we have made age a string before
print(age + "1")

#parts below are not from tutorial are are my personal bs. you are excused
# trying out when a string is converted into boolean 
#when written something it will return true otherwise false

new_string = "test"
print(type(new_string))
#lets convert it to boolean
new_string = bool(new_string)
print(new_string)


# A random text to see if a int i converted into string can be returned to int
tryout_int = 19
print(type(tryout_int))
tryout_int = str(tryout_int)
print(type(tryout_int))
print(tryout_int)
tryout_int = int(tryout_int)
print(tryout_int)
print(type(tryout_int))
#huhhhhhhhhhh??????? it worked????? i thought it wont tf
#okay one more try 
tryout_str = "19"
print(type(tryout_str))
tryout_str = int(tryout_str)
print(tryout_str)

#tf it worked again 
#i guess i kinda get it now

#tryout_str_two = "19XD"
#tryout_str_two = int(tryout_str_two)
#print(tryout_str_two)

#hehehe it finally crashed..... i guess when a string contains only numbers then we can convert it into int but as soon as it contain a letter it wont 

#lets try it with float
tryout_float = 7.9
tryout_float = str(tryout_float)
print(tryout_float)
tryout_float = float(tryout_float)
print(tryout_float)
#okay it works....now reverse
tryout_string_three = "6.9"
tryout_string_three = float(tryout_string_three)
print(tryout_string_three)
print(type(tryout_string_three))
#ooof it works again. i must be god.......wait lets check this 

#tryout_string_four = "1.9"
#tryout_string_four = int(tryout_string_four)
#print(tryout_string_four)
#so when a "." is there in a string we can not convert it into int but can into float (assumin there is no letter ofcourse Mr.obvious)

#lets see turning int into boolean 
trial_int = 1
trial_int = bool(trial_int)
print(trial_int)
#so if 0 its false other than 0 its true 
# now with float
trial_float = 0.000001
trial_float = bool(trial_float)
print(trial_float)
#so until there is a value it will be true
