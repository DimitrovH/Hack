n = input("Enter a number: ")
n = int(n)

print("Counting from 1 to " + str(n))

counter = 1

while counter <= n:
	print(counter)
	counter += 1

print("Counting from " + str(n) + " to 1")

counter = n

while counter >= 1:
	print(counter)
	counter -= 1