from codecs import charmap_build


print("Program started!")
char =input("Please enter a standard character\n")
if len(char)==1:
    print("The ASCII code for {0} is {1}".format(char, ord(char)))
else:
    print("Enter a character!")
print("Program ended!")
