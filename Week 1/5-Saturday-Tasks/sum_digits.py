n = input("Enter a number: ")
n = int(n)

total_sum = 0

while n != 0:

	counter = n % 10
	total_sum += counter

	n = n // 10

print("The sum of all digits is: " + str(total_sum))