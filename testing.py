from age_func import age_status

first_name = input("first name: ")
last_name = input("last name: ")
birth_year = int(input("birth year: "))
age = 2024 - birth_year
print(first_name)
print('Hello ' + first_name + ' ' + last_name + ', you are ' + str(age) + ' years old')
print(age_status(age))
