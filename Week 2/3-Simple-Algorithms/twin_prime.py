p = input("Enter a number: ")
p = int(p)

q1 = p + 2
q2 = p - 2

p_prime = True
counter = 2
while counter < p:
    if p % counter == 0:
        p_prime = False
        break
    counter += 1

q2_prime = True
counter = 2

while counter < q2:
    if q2 % counter == 0:
        q2_prime = False
        break
    counter += 1

q1_prime = True
counter = 2

while counter < q1:
    if q1 % counter == 0:
        q1_prime = False
        break
    counter += 1

if p_prime and (not q2_prime) and (not q1_prime):
    print(str(p) + " is prime")
    print("But " + str(q2) + " and " + str(q1) + " are not.")
elif p_prime:
    if q2_prime:
        print(q2, p)
    if q1_prime:
        print(p, q1)
else:
    print(str(p) + " is not prime.")