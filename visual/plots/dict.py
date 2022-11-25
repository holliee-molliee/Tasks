import matplotlib.pyplot as plt
import random
def data():
    paths={}
    line = input("What type of line would you like?\n")
    colour = input("What color would you like?\n")
    marker = input("What type of marker would you like?\n")
    paths["line"]=line
    paths["marker"] = marker
    paths["colour"]=colour
    return paths

def generate():
    num = int(input("How many lines would you like to display?\n"))
    for i in range(num):
        values = data()
        values_x = random.sample(range(0, 100), num)
        values_y = random.sample(range(0, 100), num)
        dane = values["colour"]+values["marker"]+values["line"]
        plt.plot(values_x,values_y, dane)
    plt.show()

def run():
    print("running...")
    generate()
    print("Done!")


if __name__=="__main__":
    run()