word= input("What strange markings do you see?\n")
print("\nIdentifying...\n")
for i in range(len(word)):
    print("Index {0}: {1}".format(i,word[i]))

print("\nDone!")