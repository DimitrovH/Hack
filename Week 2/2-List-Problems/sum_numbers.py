n = input("Enter count of numbers: ")
n = int(n)

counter = 0
sum_num = 0

while counter < n:
    number = input()
    number = int(number)

    counter += 1

    sum_num += number

print("The sum is: " + str(sum_num))