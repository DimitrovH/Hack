n = input("Enter a number: ")
n = int(n)

counter = 0
count_list = []

while counter < n:
	counter += 1

	if n % counter == 0 and n != counter:
		count_list += [counter]

sum_divisors = 0
for number in count_list:
	sum_divisors += number

print(sum_divisors)