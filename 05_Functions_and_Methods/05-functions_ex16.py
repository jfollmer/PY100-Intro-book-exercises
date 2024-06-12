# Functions and Methods chapter, exercise 16:
# In the code shown below, identify all of the function names and parameters 
# present in the code. Include the line numbers for each item identified.

def multiply(left, right):  # multiply (functin name), left, right (parameters)
    return left * right     # left, right (parameters)

def get_num(prompt):        # get_num (function name), prompt (parameter)
    return float(input(prompt)) # float (function name), input (function name),
                                # prompt (parameter)

first_number = get_num('Enter the first number: '    # get_num (function name)
second_number = get_num('Enter the second number: ') # get_num (function name)
product = multiply(first_number, second_number)      # multiply (function name)
print(f'{first_number} * {second_number} = {product}')  # print (function name)