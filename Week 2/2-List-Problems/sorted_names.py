n = input("Enter a number: ")
n = int(n)

counter = 0
name_list = []

while counter < n:
	name = input()
	name_list += [name]
	counter += 1

print("Sorted names are: ")

for name in sorted(name_list):
	print(name)