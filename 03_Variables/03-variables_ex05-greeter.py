# Variables chapter, exercise 5:
# Write a program named greeter.py that greets 'Victor' three times. Your 
# program should use a variable and not hard code the string value 'Victor' 
# in each greeting. Here's an example run of the program:

# $ python greeter.py
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.


# My solution:

name = 'Victor'

print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')


# A different given solution:
# This solution uses f-string interpolation
name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')