print("Program started!")
char = abs(int(input("Please enter an ASCII code\n")))
if char >=32 and char <=126:
    print("The character represented by the ASCII code {} is {}".format(char,chr(char)))
else:
    print("Please enter a number in this range <32,126>")
print("Program ended!")
