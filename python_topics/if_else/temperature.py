print("Lets calculate temperatures (celcious/fahrenheit)")
input_temperature = float(input("Enter your temperature:"))
input_scale = input("Enter the scale (C / F)")
output_temperature = 0
if input_scale == "c" :
    output_temperature = round((input_temperature * (9/5)) + 32 ,1)
    output_scale = "*f"
    last_print = True
elif input_scale == "f" : 
    output_temperature = round((input_temperature - 32) * (5/9) , 1) 
    output_scale = "*C"
    last_print = True
else :
    print("invalid degree")
    last_print = False

if last_print :
    print(f"{input_temperature}{input_scale} is equal to {output_temperature}{output_scale}")
# insted of last_print variable we could just print the last line in both the loops insted of outside the loop lol
 # alt + 0176 = ° 