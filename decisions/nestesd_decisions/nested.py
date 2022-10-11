type = input("What type of cover does the book have?")
if type=="soft":
    perf = input("Is the book perfect-bound?")
    if perf=="yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif type=="hard":
    print("Books with hard covers can be more expensive!")

