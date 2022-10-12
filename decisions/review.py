age = int(input("How old are you?\n"))
if age>0 and age<=1:
    print("So you are an infant")
elif age>1 and age<=9:
    print("So you are a child")
elif age>9 and age<=19:
    print("So you are a teenager")
elif age>19 and age<=29:
    print("So you are young adult")
elif age>29 and age<=65:
    print("So you are an adult")
else:
    print("So you are a senior")