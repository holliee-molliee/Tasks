def search(path):
    print("Searching...")
    with open(path,'r') as file:
        for line in file:
            print("Looked in {}".format(line))
    print("Done!")

def run():
    search("library.txt")

if __name__=="__main__":
    run()