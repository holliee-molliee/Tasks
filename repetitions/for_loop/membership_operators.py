from cmath import phase


phrase = input("What phrase do you see?\n")
print("\n\nReversing...\n")
change=''
for letter in phrase:
    change=letter+change #Adding letter at the beggining of the string
print("The phrase is: ",change)