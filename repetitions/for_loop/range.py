lvl = int(input("What level of brightness is required?\n"))
print("Adjusting brightness...")
for i in range(2,lvl+2,2):
    lvl_br = "*"*i
    print("Beep's brightness level:",lvl_br)
    print("Bop's brightness level:",lvl_br)

print("Adjustments complete!")