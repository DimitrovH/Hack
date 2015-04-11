string = input("Enter a string: ")

vowels = "aeiouyAEIOUY"
counter = 0

for ch in string:
    if ch in vowels:
        counter += 1

print(counter)