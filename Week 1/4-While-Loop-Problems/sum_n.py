n = input("Enter a number: ")
n = int(n)

total_sum = 0
counter = 1

while counter <= n:
	total_sum += counter
	counter += 1

print("The sum of all digits is: " + str(total_sum))