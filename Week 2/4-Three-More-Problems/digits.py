n = input("Enter a number: ")
n = int(n)


digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10

print("The list of digits is: " + str(digits))


number = 0

for digit in digits:
    number = number * 10 + digit

print("The number is: " + str(number))