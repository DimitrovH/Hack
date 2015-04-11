n = input("Enter count of numbers: ")
n = int(n)

counter = 0
min_list = []

while counter < n:
    number = input()
    number = int(number)

    counter += 1

    min_list += [number]

print("Min is: " + str(min(min_list)))