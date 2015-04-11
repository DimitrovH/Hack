a = input("Enter the lower bound of the interval: ")
a = int(a)

b = input("Enter the upper bound of the interval: ")
b = int(b)

x = input("Enter a number: ")
x = int(x)

if x == a:
	print("The number is equal to the lower bound of the interval.")
elif x == b:
	print("The number is equal to the upper bound of the interval.")
elif x > a and x < b:
	print("The number is in the interval.")
elif x < a:
	print("The number is outside the interval, " + str(x) + " < " + str(a) + ".")
elif x > b:
	print("The number is outside the interval, " + str(x) + " < " + str(a) + ".")