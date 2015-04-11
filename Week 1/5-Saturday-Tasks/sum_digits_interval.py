N = input("Enter N: ")
N = int(N)

M = input("Enter M: ")
M = int(M)

n = N

while n <= M:
	counter = n % 10 + n // 10
	print("The sum of digits of " + str(n) + " = " + str(counter))
	n += 1















# n = M
# total_sum = 0

# while n != N:

# 	counter = n % 10
# 	total_sum += counter
# 	n = n // 10

# print(total_sum)