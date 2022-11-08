def movements():
    path = [ "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    var = movements()
    for i in range(0,len(var),2):
        print(f"{var[i]} for {var[i+1]} steps")

if __name__=="__main__":
    run()