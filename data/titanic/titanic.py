import csv
records = []
headings=[]

def load_data(file_path):
    print("Loading data...",end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for line in csv_reader:
            records.append(line)
    print("Done!")

def display_menu():
    action = int(input("Please select one of the following options:\n[1] Display the names of all passengers\n[2] Display the number of passengers that survived\n[3] Display the number of passengers per gender\n[4] Display the number of passengers per age group\n[5]Display the number of survivors per age group\n\n"))
    return action

def display_passenger_names():
    print("The names of passengers are...\n")
    for record in records:
        passenger_name=record[3]
        print(passenger_name)

def display_num_survivors():
    num_survived=0
    for record in records:
        survival_status=record[1]
        if int(survival_status)==1:
            num_survived+=1
    print(f"{num_survived} passengers survived.")

def display_passengers_per_gender():
    females,males=0,0
    for record in records:
        gender = record[4]
        if gender=="female":
            females+=1
        elif gender=="male":
            males+=1
    print(f"females: {females}, males: {males}")

def display_passengers_per_age_group():
    children,adults,elderly=0,0,0
    for record in records:
        if len(record[5])==0:
            continue
        else:
            age = float(record[5])
            if age<18:
                children+=1
            elif age>=18 and age<65:
                adults+=1
            else:
                elderly+=1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

def display_survivors_per_age_group():
    children,adults,elderly=0,0,0
    num_c_sur,num_a_sur,num_e_sur=0,0,0
    for record in records:
        survival_status=record[1]
        if int(survival_status)==1:
            if len(record[5])==0:
                continue
            else:
                age = float(record[5])
                if age<18:
                    num_c_sur+=1
                elif age>=18 and age<65:
                    num_a_sur+=1
                else:
                    num_e_sur+=1
        if len(record[5])==0:
            continue
        else:
            age = float(record[5])
            if age<18:
                children+=1
            elif age>=18 and age<65:
                adults+=1
            else:
                elderly+=1
    print(f"children: {num_c_sur}/{children}, adults: {num_a_sur}/{adults}, elderly: {num_e_sur}/{elderly}")

def run():
    load_data("titanic.csv")
    print(f"Succesfully loaded {len(records)}\n")
    selected_option = display_menu()
    print(f"You have selection option: {selected_option}\n")
    if selected_option==1:
        display_passenger_names()
    elif selected_option==2:
        display_num_survivors()
    elif selected_option==3:
        display_passengers_per_gender()
    elif selected_option==4:
        display_passengers_per_age_group()
    elif selected_option==5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognized")

if __name__=="__main__":
    run()
