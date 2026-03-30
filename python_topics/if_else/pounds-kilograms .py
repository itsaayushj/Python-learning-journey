print("Pounds/kilograms converter")
weight = float(input("Enter the weight"))
unit = input("Enter the unit (kg / pound):")
converted_weight = 0
if unit == "kg" :
    converted_weight = weight * 2.20462
    converted_unit = "pound"   # i declared it because to add it in final line output
    final_statment = True
elif unit == "pound" :
    converted_weight = weight * 0.453592
    converted_unit = "kg"
    final_statment = True

else :
    print("Unit is invalid")
    final_statment = False

if final_statment : 
    print(f"{weight}{unit} is equal to {converted_weight}{converted_unit}" )
    