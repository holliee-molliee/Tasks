def likelihoods():
    likelihoods=(50, 38, 27, 99, 4)
    return min(likelihoods)

def run():
    tuple= likelihoods()
    print(f"Minimum likelihood of fallig: {tuple}%")

if __name__=="__main__":
    run()