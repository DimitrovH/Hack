#"a" is the lower bound of the interval and "b" is the upper one.

a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

counter = a 

while counter <= b:

	if counter % 2 == 0:
		print(str(counter) + " is even.")
	else:
		print(str(counter) + " is odd.")

	counter += 1
