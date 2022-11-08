def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left","Trun Right"]
    return directions

def menu():
    print("Please select a direction: ")
    dir = directions()
    lp = 0
    for i in dir:
        print(f"{lp}: {i}")
        lp+=1
    which = int(input())
    return dir[which]

def run():
    route=[]
    print("Working out escape route...")
    for i in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__=="__main__":
    run()