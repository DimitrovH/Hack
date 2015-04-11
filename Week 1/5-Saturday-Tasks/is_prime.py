n = input("Enter a number: ")
n = int(n)

counter = 2
is_prime = True

if n == 1:
    is_prime = False

while counter < n:

	if n % counter == 0:
		is_prime = False
		break
	counter = counter + 1

if is_prime == True:
    print(str(n) + " is a prime number.")
else:
    print(str(n) + " isn't a prime number.")