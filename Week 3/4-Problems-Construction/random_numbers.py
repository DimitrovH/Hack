from random import randint

def generate_random_list(number, start, end):
    result = []
    counter = 0

    while counter < number:
        next_number = randint(start, end)
        result = result + [next_number]

        counter += 1
        
    return result

print(generate_random_list(4,100,150))