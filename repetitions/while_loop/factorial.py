from math import factorial


num = int(input("Please enter a number?\n"))
iter=0
fact = 1
while iter<num:
    iter+=1
    fact*=iter
print("The factorial is {}".format(fact))