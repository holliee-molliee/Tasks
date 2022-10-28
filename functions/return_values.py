def sum_weights(w_beep, w_bop):
    sum = w_beep+w_bop
    return sum

def calc_avg_weight(w_beep2,w_bop2):
    avg = sum_weights(w_beep2,w_bop2)/2
    return avg

def run():
    weight1= int(input("What is the weight of Beep?\n"))
    weight2=int(input("What is the weight of Bop?\n"))
    what = input("What would you like to calculate?(sum or average)?\n")
    if what=="sum":
        sum_w=sum_weights(weight1,weight2)
        print("The sum of Beep's and Bop's weight is {}".format(sum_w))
    else:
        avg_w=calc_avg_weight(weight1,weight2)
        print("The average of Beep's and Bop's weight is {}".format(avg_w))
run()