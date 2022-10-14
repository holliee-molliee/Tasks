from operator import index


#1 option with nested loops
seq = input("Please enter a sequence\n")
mark = input("Please enter the character for the marker\n")
dis=0
for i in range(len(seq)):
    if seq[i]==mark:
        for j in range(i+1,len(seq)-1):
            if seq[j]==mark:
                break
            else:
                dis+=1
        break
print("The distance between the markers is", dis)
#2 option with a list
seq = input("Please enter a sequence\n")
mark = input("Please enter the character for the marker\n")
lol=[]
for i in range(len(seq)):
    if seq[i]==mark:
        lol.append(i)
dis=lol[1]-lol[0]-1
print("The distance between the markers is ", dis)
    