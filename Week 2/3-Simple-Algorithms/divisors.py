n = input("Enter a number: ")
n = int(n)

counter = 0
count_list = []

while counter < n:
	counter += 1

	if n % counter == 0 and n != counter:
		count_list += [counter]

print("Divisors are:")

for number in count_list:
	print(number)
