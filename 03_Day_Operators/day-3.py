# Day 3 Exercises
my_age =  24
my_height = float(180)
com_number = 2+3j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
b = int(input("Enter the length 2nd side  of traingle: "))
c = int(input("Enter the length 3nd side  of traingle: "))

perimeter_triangle = base+b+c

print("The perimeter of the triangle is: ", perimeter_triangle)

area_traingle = 0.5*base*height

print("The area of the traingle is ", int(area_traingle))

length = int(input("Enter length: "))
width = int(input("Enter length: "))

perimeter_rectangle = 2*(length+width)

print("The perimeter of the triangle is: ", int(perimeter_rectangle))

len_python = len('python')
len_dragon = len('dragon')

print(len_dragon is not len_python)

on_in = ('on' in 'python') and ('on' in 'dragon')

print(on_in)

sentence = "I hope this course is not full of jargon"

jargon_in = 'jargon' in sentence

print(jargon_in)

print(str(len('python')))

print(7//2 == int(2.7))

print(7//2 == int(2.7))

type('10') == type(10)

int(9.8) == 10

work_hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))

weekly_earning = work_hours*rate_per_hour

print("Your weekly earning is: ", weekly_earning)

seconds_per_year = 365*24*3600
seconds_100_years = 100*seconds_per_year

num_years_lived = int(input("Enter number of years you have lived: "))

num_seconds_tolive = seconds_100_years - num_years_lived*seconds_per_year

print("You have lived for", num_seconds_tolive, "seconds")

for i in range(1, 6):
    print(i, 1, i, i*i, i*i*i)
