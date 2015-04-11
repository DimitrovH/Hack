n = input("Enter count of numbers: ")
n = int(n)

counter = 0
even_counter = []

while counter < n:
    number = input()
    number = int(number)
    
    if number % 2 == 0:
        even_counter = even_counter + [number]

    counter += 1

print("Count of evens: " + str(len(even_counter)))
print("Evens are: ")

for even in even_counter:
    print(even)