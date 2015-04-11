def max_score(beers, fries):

    total_sum = 0
    index = 0

    beers = sorted(beers)
    fries = sorted(fries)
    
    
    for index in range(0, len(beers)):
            total_sum += beers[index] * fries[index]
    
    return total_sum

print(max_score([5,7], [5,2]))