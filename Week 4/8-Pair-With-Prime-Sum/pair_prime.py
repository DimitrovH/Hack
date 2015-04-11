def is_prime(n):

    counter = 2
    is_prime = True

    if n == 1:
        is_prime = False

    while counter < n:
        if n % counter == 0:
            is_prime = False
            break
        counter = counter + 1

    return is_prime


def prime_pair(numbers):
    
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                return True

    return False

print(prime_pair([1,4,2,5,7]))