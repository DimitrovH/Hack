def divisors(n):
    result = []

    counter = 1

    while counter < n:
        if n % counter == 0:
            result = result + [counter]

        counter += 1

    return result


def sum_ints(numbers):
    result = 0

    for number in numbers:
        result += number

    return result

n = input("Enter a number: ")
n = int(n)

print(sum_ints(divisors(n)))

def sum_divisors(n):

    return sum_ints(divisors(n))

def is_perfect(n):

    return sum_divisors(n) == n

n = input("Enter a number: ")
n = int(n)

if is_perfect(n) == True:
    print(str(n) + " is perfect!")
else:
    print(str(n) + " is not perfect!")

n = input("Enter a number: ")
n = int(n)

start = 6

while True:
    
    if is_perfect(start):
        print(start)
        n = n - 1

    if n == 0:
        break

    start += 1

def is_prime(n):
    if n <= 1:
        return False

    is_prime = True

    start = 2

    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
    
    return is_prime


def to_digits(n):
    result = []
    
    while n != 0:
        digit = n % 10
        
        result = [digit] + result

        n = n // 10

    return result


n = input("Enter n: ")
n = int(n)

digits = to_digits(n)

prime_digit = False

for digit in digits:
    if is_prime(digit):
        prime_digit = True
        break

if prime_digit == True:
    print("There are prime digits!")
else:
    print("There are no prime digits!")

p = input("Enter number: ")
p = int(p)

q = p - 2
r = p + 2

is_p_prime = is_prime(p)
is_q_prime = is_prime(q)
is_r_prime = is_prime(r)

if is_p_prime and (not is_q_prime) and (not is_r_prime):
    print(str(p) + " is prime")
    print("But " + str(q) + " and " + str(r) + " are not.")
elif is_p_prime:
    if is_q_prime:
        print(q, p)
    if is_r_prime:
        print(p, r)
else:
    print(str(p) + " is not prime.")