n = input("Enter a number: ")
n = int(n)

counter = 1
product = 1

while counter <= n:
    product = product * counter
    counter = counter + 1

print("The factorial of " + str(n) + " = " + str(product))