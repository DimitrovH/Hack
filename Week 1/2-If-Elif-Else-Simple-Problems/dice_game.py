from random import randint

n = input("Enter sides: ")
n = int(n)

first_player = input("Player 1, enter your name: ")
second_player = input("Player 2, enter your name: ")

dice_1 = randint(1,n)
dice_2 = randint(1,n)

print(first_player + " rolled: " + str(dice_1))
print(second_player + " rolled: " + str(dice_2))

if dice_1 > dice_2:
	print(first_player + " is winner.")
elif dice_2 > dice_1:
	print(second_player + " is winner.")
else:
	print("Tie! Unfortunately there is no winner.")