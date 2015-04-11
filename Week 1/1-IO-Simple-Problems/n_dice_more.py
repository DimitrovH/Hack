from random import randint

n = input("Enter a number: ")
n = int(n)

dice_1 = randint(1,n)
print("First roll: " + str(dice_1))

dice_2 = randint(1,n)
print("Second roll: " + str(dice_2))

dice_3 = randint(1,n)
print("Third roll: " + str(dice_3))

all_rolls = dice_1 + dice_2 + dice_3
print("Total sum of all rolls is: " + str(all_rolls))