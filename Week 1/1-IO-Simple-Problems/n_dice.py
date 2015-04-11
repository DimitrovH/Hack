from random import randint

n = input("Enter sides: ")
n = int(n)

dice = randint(1,n)

print("You rolled: " + str(dice))