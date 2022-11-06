import csv

def export(path,num):
    print("Exporting...")
    with open(path,"a") as file:
        for i in range(num):
            bot_id=int(input("Please enter the bot id: \n"))
            bot_name = input("Please enter the bot name:\n")
            bot_paint = input("Please enter the bot paint:\n")
            file.write(f"{bot_id},{bot_name},{bot_paint}\n")

    print("Done!")

def run():
    export("exported_bots.csv", 2)

if __name__=="__main__":
    run()