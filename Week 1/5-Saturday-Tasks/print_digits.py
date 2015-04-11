n = input("Enter a number: ")
n = int(n)

while n != 0:

	counter = n % 10

	print(counter)

	n = n // 10