how_many = int(input("How many numbers should i sum up?\n"))
iter = 0
sum=0
while iter<how_many:
    iter+=1
    num= int(input("Please enter number {0} of {1}\n".format(iter, how_many)))
    sum+=num
print("The answer is {}".format(sum))