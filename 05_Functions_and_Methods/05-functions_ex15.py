# Functions and Methods chapter, exercise 15:
# Using the code below, classify the identifiers as global, local, or built-in.
# For our purposes, you may assume this code is the entire program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# line 5: multiply (global), left (local), right(local)
# line 6: left (local), right (local)
# line 8: get_num (global), prompt (local)
# line 9: float (built-in), input(built-in), prompt (local)
# line 11: first_number (global), get_num (global)
# line 12: second_number (global), get_num (global)
# line 13: product (global), multiply (global), first_number (global),
#          second_number (global)
# line 14: print (built-in), first_number (global), second_number (global),
#          product (global)