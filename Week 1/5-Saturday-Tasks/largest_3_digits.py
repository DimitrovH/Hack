n = input("Enter a 3-digit number: ")
n = int(n)

z = n % 10
n = n // 10

y = n % 10
n = n // 10

x = n % 10
n = n // 10

print(x,y,z)

largest = x

if y >= largest and y >= z:
	largest = y

if z >= largest and z >= y:
	largest = z

print("The largest digit is: " + str(largest))

smallest = x

if y <= smallest and y <= z:
	smallest = y

if z <= smallest and z <= y:
	smallest = z

print("The smallest digit is: " + str(smallest))

middle = x

if (largest == x and smallest == y) or (largest == y and smallest == x):
	middle = z
elif (largest == z and smallest == x) or (largest == x and smallest == z):
	middle = y

max_num = largest * 100 + middle * 10 + smallest
min_num = smallest * 100 + middle * 10 + largest

print("The largest number with those digits is: " + str(max_num))
print("The smallest number with those digits is: " + str(min_num))
