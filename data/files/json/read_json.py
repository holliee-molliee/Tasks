import json

def read(path):
    with open(path) as file:
        data = json.load(file)
        city_name = data["city"]
        print(f"City Name: {city_name}")
        population = data["population"]
        print(f"Popilation Size: {population}")
        bots = data["bots"]
        for bot in bots:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")

def run():
    read("robocity.json")

if __name__=="__main__":
    run()