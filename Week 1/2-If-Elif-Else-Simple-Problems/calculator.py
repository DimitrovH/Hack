a = input("Enter a number: ")
a = int(a)

b = input("Enter a number: ")
b = int(b)

oper = input("Enter an operation: ")

if oper == "+":
	print("The result is: " + str(a + b))
elif oper == "-":
	print("The result is: " + str(a - b))
elif oper == "/":
	print("The result is: " + str(a / b))
elif oper == "*":
	print("The result is: " + str(a * b))
else:
	print("We do not support that operation.")