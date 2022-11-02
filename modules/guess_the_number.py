def play_guess_the_number(): 
    import random
    min_val = int(input("Please enter minimum value: \n"))
    max_val = int(input("Please enter maximum value:\n"))
    number = random.randrange(min_val,max_val, 1)
    guess = int(input(f"I am thinking of a number between {min_val} and {max_val}.  Can you guess what it is?\n"))
    while guess!=number:
        if guess<number:
            print("Your guess is too low.")
        elif guess>number:
            print("Your guess is too high.")
        guess = int(input("Try again:\n"))
    print("Congratulations! You guessed my number!")

play_guess_the_number()