n = input("Enter count of numbers: ")
n = int(n)

counter = 0
avg_counter = 0
avg_sum = 0

while counter < n:
    number = input()
    number = int(number)

    counter += 1

    avg_counter += number
    avg_sum = avg_counter / counter

print(avg_sum)