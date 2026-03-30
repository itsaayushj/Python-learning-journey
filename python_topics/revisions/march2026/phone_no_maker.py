import random
def phno_maker( area_code , first_4 ,country_code = 99) : 
    last_4 = random.randint(0000 , 9999)
    print(country_code , area_code , first_4 , last_4 , sep= "-")

phno_maker(26 , 9999)
