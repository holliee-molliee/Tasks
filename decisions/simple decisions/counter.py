num1 = int(input("Please enter the first number. "))
num2 = int(input("Please enter the second number. "))
num3 = int(input("Please enter the third number. "))

even=0
odd=0
if num1%2==0:
    even+=1
else:
    odd+=1
if num3%2==0:
    even+=1
else:
    odd+=1
if num2%2==0:
    even+=1
else:
    odd+=1

print("There were {} even and {} odd numbers".format(even, odd))