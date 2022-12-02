import matplotlib.pyplot as plt

def read_data(path):
    temps=[]
    with open(path) as file:
        for line in file:
           temps.append(int(line.strip()))

    return temps

def run():
    data=read_data("temps.txt")
    days = [1,2,3,4,5,6,7]
    fig, (axs1,axs2) = plt.subplots(1,2)
    axs1.plot(days,data)
    axs2.bar(days,data)
    plt.show()

run()

