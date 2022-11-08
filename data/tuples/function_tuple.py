def likelihood():
    likelihood=(50, 38, 27, 99, 4)
    return (min(likelihood),max(likelihood))

def run():
    tuple= likelihood()
    print(f"Minimum likelihood of fallig: {tuple[0]}%")
    print(f"Maximum likelihood of fallin: {tuple[1]}%")
if __name__=="__main__":
    run()