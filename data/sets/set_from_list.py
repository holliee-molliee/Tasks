def observed():
    observations =[]
    for i in range(7):
        value = input("Please enter an observation:\n")
        observations.append(value)
    return observations


def run():
    print("Counting observations...")
    obs = observed()
    ok = set()
    for elem in obs:
        ok.add((elem, obs.count(elem)))
    for i in ok:
        print(f"{i[0]} observed {i[1]} times.")

if __name__=="__main__":
    run()