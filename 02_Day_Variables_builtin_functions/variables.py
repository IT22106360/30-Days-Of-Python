#Day 2: 30 Days of python programming

first_name = 'Rashmika'
last_name = 'Rupasinghe'
full_name = 'Rashmika Rupasinghe'
country = 'Sri Lanka'
city = 'Colombo'
age = 24
year = '2001'
is_married = False
is_true = True
is_light_on = False
skills, is_mingle = ['HTML', 'CSS', 'JS', 'React', 'Python'], False
person_info = {
    'firstname': 'Rashmika',
    'lastname': 'Rupasinghe',
    'country': 'Sri Lanka',
    'city': 'Colombo' 
}

print(first_name, last_name, country, age, is_married, is_true, is_light_on, skills,is_mingle, person_info)

print(*(type(v) for v in [
    first_name, last_name, full_name, country, city, age, year,
    is_married, is_true, is_light_on, skills, is_mingle, person_info
]))

print('first name length: '+ str(len(first_name)))
print('last name length: '+ str(len(last_name)))

num_one = 5
num_two = 4

diff = num_one - num_two
print(diff)

product = num_one*num_two
print(product)

divisions = num_one/num_two
print(divisions)

remainder= num_one%num_two
print(remainder)

exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)

radius = float(input("Enter the radius: "))
pi = 3.14

area_of_circle = pi*radius**2
circum_of_circle = 2*pi*radius

print('area: '+ str(area_of_circle))
print('circumference: '+str(circum_of_circle))

first_name = input("first name: ")
last_name = input("last name: ")
country = input("country: ")
age = int(input("Age: "))

print(first_name, last_name, country, age)

help('keywords')
