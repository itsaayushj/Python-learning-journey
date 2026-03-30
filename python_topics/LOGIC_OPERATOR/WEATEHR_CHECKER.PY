print(" Lets check weather ")
temperature = float (input("What is today's temperature? (in Celsius)"))
sun_input = input("Is it sunny outside (Y/N)")
if sun_input == "Y":
    sun = True
elif sun_input == "N":
    sun = False
else :
    print("your sun is invalid")


if sun_input == "Y" or sun_input == "N":
    if temperature >= 35 and sun :
     print("It is hot and sunny outside ☀️🥵")
    elif 35 > temperature > 10  and sun :
     print("it is sunny but moderate outside ☀️😎")
    elif temperature <= 10  and sun :
     print("Even though sun is there it is cold out there☀️🥶 ")
    elif temperature >= 35 and not sun :
     print("It is hot and cloudy outside ☁️🥵")
    elif 35 > temperature > 10  and not sun :
     print("it is cloudy and moderate outside ☁️😎")
    elif temperature <= 10  and not sun :
      print("As sun is not outside  it is cold out there☁️🥶 ")
    else :
     pass

print(" Thanks dumbass!")

# without sun_input it was not working properly if sun input is outer than x or y it would just assume as True