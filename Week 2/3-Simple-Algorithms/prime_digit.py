num = input("Enter a number: ")
num = int(num)

digits = []

while num != 0:
    digit = num % 10

    digits = [digit] + digits 

    num = num // 10

prime_digit = False

for digit in digits:
    if digit in [2, 3, 5, 7]:
        prime_digit = True
        break

if prime_digit == True:
    print("At least one prime digit was found.")
else:
    print("No prime digits were found.")
