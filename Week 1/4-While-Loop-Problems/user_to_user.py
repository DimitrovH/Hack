a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if a > b:
	counter = b
	while counter <= a:
		print(counter)
		counter += 1

if a < b:
	counter = a
	while counter <= b:
		print(counter)
		counter += 1
