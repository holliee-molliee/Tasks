from pydoc import cli


def climb_ladder(num_rem, num_crossed):
    if num_rem>num_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5,2)
climb_ladder(2,5)