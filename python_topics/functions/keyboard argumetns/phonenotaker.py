import random
def get_phone() : 
    country_code = int(input("Enter your country code : "))
    area_code = int(input("Enter your area code : "))
    first_4_digit = int(input("Enter your first four digits you want : "))
    last_4_digits = random.randint(1000 , 9999)
    num = f"{country_code} - {area_code} - {first_4_digit} - {last_4_digits}"
    return country_code , area_code , first_4_digit , last_4_digits , num 

# _ , _ , _ , _ , num = get_phone() 
# *_ , num = get_phone() 
*rest , num = get_phone()
print(num)





