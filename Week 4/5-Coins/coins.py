def calculate_coins(sum_coins):

    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum_coins = round(sum_coins * 100)

    
    for item in coins:
        result[item] = sum_coins // item
        sum_coins = sum_coins % item
    return result

n = input("Enter a float number: ")
n = float(n)

print(calculate_coins(n))