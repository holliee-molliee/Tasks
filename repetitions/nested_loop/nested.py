row = int(input("How many rows should I have?\n"))
column = int(input("How many columns should I have?\n"))
print("Here I go:")
for i in range(row): #loop  that goes through rows
    for j in range(column): #loop that goes through columns
        print(":-)", end=" ")
    print()
print("Done!")
        