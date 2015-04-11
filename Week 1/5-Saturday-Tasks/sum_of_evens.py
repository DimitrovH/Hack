n = input("Enter a number: ")
n = int(n)

total_sum = 0
counter = 1

while counter <= n:

	if counter % 2 == 0:
		total_sum += counter
	counter += 1

print("The sum of even numbers is: " + str(total_sum))