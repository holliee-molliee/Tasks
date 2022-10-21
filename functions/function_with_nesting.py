from xml.dom import InuseAttributeErr


def identify():
    thing = input("What lies before us?\n")
    if thing=="a large boulder":
        print("It's time to run")
    else:
        print("We will be fine")
    
identify()
