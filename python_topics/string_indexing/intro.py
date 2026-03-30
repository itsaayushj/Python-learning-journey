# indexing = accessing element of sequence by []
#       [start : end : step]
# doesnt works on intigers 
roll_number = "123-456-789"  # the start digit is included while the end digit is exclud
last_digits =roll_number[-3:]
print(f" Your id is : ***-***-{last_digits}")


# ommiting 3 digits 
#numbers = "123456789"
#print(numbers[0:9:3]) # every 3rd digit will be counted 