n = input("Enter a number: ")
n = int(n)

rev_number = 0
non_reversed = n

while n != 0:
    digit = n % 10

    rev_number = rev_number * 10 + digit

    n = n // 10

if non_reversed == rev_number:
    print(str(non_reversed) + " is a palindrom.")
else:
    print(str(non_reversed) + " is not a palindrom.")