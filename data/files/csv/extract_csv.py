import csv
def exctract(path):
    print("Extracting...")
    with open("bots.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        names = ""
        for value in csv_reader:
            names+=value[1]
            names+="\n"
        print("Done! The extracted names are as follows:")
        print(names[:-1])

def run():
    exctract("bots.csv")

if __name__=="__main__":
    run()
