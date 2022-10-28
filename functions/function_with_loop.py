def cross_bridge(steps):
    if steps>5:
        for step in range(steps):
            print("Crossed step!")
        print("The bridge is collapsing!")
    else:
        for step in range(steps):
            print("Crossed step!")
        print("We must keep going!")
        
cross_bridge(3)
cross_bridge(6)
    
