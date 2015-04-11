from random import randint

maria_scores = 1001
ivan_scores = 1001

while True:

    counter = 1
    dice_roll_sum = 0

    while counter <= 5:
        dice_roll = randint(1, 6)        
        dice_roll_sum += dice_roll
        counter += 1
        
    if maria_scores > 0:
        maria_scores -= dice_roll_sum
    elif maria_scores < 0:
        maria_scores += dice_roll_sum

    print("Maria rolls: " + str(dice_roll_sum) + " and has a score of: " + str(maria_scores))
    
    if maria_scores == 0:
        break

    counter = 1
    dice_roll_sum = 0
    
    while counter <= 5:
        dice_roll = randint(1, 6)
        dice_roll_sum += dice_roll
        
        counter += 1
        
    if ivan_scores > 0:
        ivan_scores -= dice_roll_sum
    elif ivan_scores < 0:
        ivan_scores += dice_roll_sum

    print("Ivan rolls: " + str(dice_roll_sum) + " and has a score of: " + str(ivan_scores))
    
    if ivan_scores == 0:
        break

if maria_scores == 0:
	print("The winner is Maria.")
elif ivan_scores == 0:
	print("The winner is Ivan.")