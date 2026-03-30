print("Lets calculate your BMI")
weight = float(input("Enter your Weight:"))
height = float(input("Enter your Height (in meter):"))
bmi = weight / height **2
print(f"Your BMI is {round(bmi , 2)}")
