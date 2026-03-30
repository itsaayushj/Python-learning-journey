import random 
def number_generator(country_code , area_code , first_four ) : 
    last_four = str(random.randint(1000 , 9999))
    return country_code + area_code + first_four + last_four 

print(number_generator("91" , "26" , "8008" ))
