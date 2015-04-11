first_name = input("Enter first name: ")
middle_name = input("Enter middle name: ")
surname = input("Enter surname: ")
birth_year = input("Enter year of birth: ")
birth_year = int(birth_year)

person = {}

person["first_name"] = first_name
person["middle_name"] = middle_name
person["surname"] = surname
person["birth_year"] = birth_year
person["age"] = 2015 - birth_year

print(person)