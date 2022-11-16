def started(msg=""): #msg="Reading data from athlete_events.csv"
    print("-"*85)
    print(f"Operation started: {msg}...\n")


def completed():
    print("\nOperation completed.")
    print("-"*85)


def error(msg): #msg="Invalid Selection!"
    print(f"Error! {msg}")

def menu():
    
    print("Please select one of the following options:")
    print(f'{"[years]":>10} List unique years')
    print(f"{'[tally]':>10} Tally up medals")
    print(f"{'[ctally]':>10} Tally up medals for each team")
    print(f"{'[exit]':>10} Exit the program")
    choice = input("Your selection: ")
    return choice

def display_medal_tally(tally):
    print(f"|{'Gold':<10}|{tally['Gold']:<10}|")
    print(f"|{'Sliver':<10}|{tally['Silver']:<10}|")
    print(f"|{'Bronze':<10}|{tally['Bronze']:<10}|")

def display_team_medal_tally(team_tally):
    emp=""
    for key,value in team_tally.items():
        print(key)
        for tally,count in value.items():
            sklejka=tally+": "+str(count)+", "
            emp+=sklejka
        print(f"\t{emp[:-2]}")

def display_years(years):
    years = sorted(years, reverse=True)

    