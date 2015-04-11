n = input("Enter count of numbers: ")
n = int(n)

counter = 0
max_list = []

while counter < n:
    number = input()
    number = int(number)

    counter += 1

    max_list += [number]

print("Max is: " + str(max(max_list)))