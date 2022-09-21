name= input("What is your name human? ")
age = int(input("How old are you?(in years) "))
height = float(input("How tall are you?(in meters) "))
weight = int(input("How much do you weight?(in kilograms) "))
bmi = round(weight/(height**2),2)
print(f"{name} you are {age} years old and your bmi is {bmi}.")

