print("Welcome to distance calculator")
input_distance = float(input("Enter the distance:"))
input_unit = input("Enter the unit of the given value (km / miles)")
output_distance = 0
if input_unit == "km":
    output_distance = input_distance / 1.609 
    to_finalise = True
    output_unit = "miles"
elif input_unit == "miles":
    output_distance = input_distance * 1.609 
    to_finalise = True 
    output_unit = "km"
else : 
    print("invalid unit")
    to_finalise = False           
     #to_finalise is the variable i gave so it dont throw error in last print statment.
if to_finalise :
    print(f"{input_distance}{input_unit} is equal to {output_distance}{output_unit}")
