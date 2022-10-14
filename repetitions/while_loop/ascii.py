
bars = int(input("How many bars should be charged?\n"))
iter = 0 #iteration variable
while iter<bars:
    iter+=1 #incrementing the variable
    bar = (chr(9608)+chr(32))*iter #using block and space code from ascii table and multiplying them with iteration variable 
    print("Charging:"+bar)
print("Battery is fully charged.")