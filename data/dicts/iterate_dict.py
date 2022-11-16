import simple_dicts as sd

def display_keys(data):
    for key in data.keys():
        print(key)

def display_values(data):
    for value in data.values():
        print(value)

def displey_items(data):
    for key,value in data.items():
        print(f"{key}: {value}")

def run():
    print("Dictionary: ")
    print(sd.pattern())
    print("\nKeys:")
    display_keys(sd.pattern())
    print("\nValues:")
    display_values(sd.pattern())
    print("\nPairs")
    displey_items(sd.pattern())

if __name__=="__main__":
    run()