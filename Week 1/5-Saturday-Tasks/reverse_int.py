n = input("Enter a number: ")
n = int(n)

rev_number = 0

while n != 0:
    digit = n % 10

    rev_number = rev_number * 10 + digit

    n = n // 10

print("The reversed number is: " + str(rev_number))