def directions():
    directions=[ "Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return directions
    
def menu():
    print("Please select direction: ")
    var = directions()
    lp=0
    for i in var:
        print(f"{lp}: {i}")
        lp+=1

def run():
    menu()

if __name__=="__main__":
    run()
