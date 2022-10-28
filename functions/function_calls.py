def ascii(word):
    dash_num = 4+len(word)
    print(dash_num*"-")
    print("| "+word+" |")
    print(dash_num*"-")
def lowerr(word):
    print(word.lower())
def upperr(word):
    print(word.upper())
def mirrored(word):
    print(word[::-1])
def repeat(word):
    step= int(input("How many times:"))
    for i in range(step):
        if i%2==0:
            lowerr(word)
        else:
            upperr(word)

def run():
    wo = input("Enter a word:\n")
    print("How would you like to display your word?")
    print("1)Display in a Box\n2)Display Lower-case\n3)Display Upper-case\n4)Display Mirrored\n5)Repeat")
    action = int(input())
    if action==1:
        ascii(wo)
    elif action==2:
        lowerr(wo)
    elif action==3:
        upperr(wo)
    elif action==4:
        mirrored(wo)
    elif action==5:
        repeat(wo)

run()