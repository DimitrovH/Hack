def square(n):

	return n*n

print(square(5))

def factorial(n):
    counter = 1
    start = 1

    while start <= n:
        counter *= start
        start += 1

    return counter

print(factorial(5))

def count_elements(items):
	counter = 0   

	for element in items:
		counter += 1

	return counter

print(count_elements([1,2,4,5]))

def member(x, xs):

	member = False

	for num in xs:
		if x == num:
			member = True
			break

	return member

print(member(3, [1,2,3]))

def grades_that_pass(students, grades, limit):

    index = 0
    result = []

    for grade in grades:
        student = students[index]
        
        if grade >= limit:
            result = result + [student]
        
        index += 1

    return result

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]
limit = 4.6
print(grades_that_pass(students,grades,limit))