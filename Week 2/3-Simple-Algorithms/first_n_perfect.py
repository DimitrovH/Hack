n = input("Enter a number: ")
n = int(n)

counter = 1

while True:

    divisors_sum = 0
    divisor = 1

    while divisor < counter:
        if counter % divisor == 0:
            divisors_sum += divisor

        divisor += 1

    if divisors_sum == counter:
        print(counter)
        n = n - 1
    
    if n == 0:
        break

    counter += 1