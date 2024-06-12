# Flow Control chapter, exercise 7:
# Write a function that takes a single integer argument and prints a message 
# that describes whether:
    # the value is between 0 and 50 (inclusive)
    # the value is between 51 and 100 (inclusive)
    # the value is greater than 100
    # the value is less than 0

                      # Print in this format:
# number_range(0)     # 0 is between 0 and 50
# number_range(25)    # 25 is between 0 and 50
# number_range(50)    # 50 is between 0 and 50
# number_range(75)    # 75 is between 51 and 100
# number_range(100)   # 100 is between 51 and 100
# number_range(101)   # 101 is greater than 100
# number_range(-1)    # -1 is less than 0


# My answer:

value = int(input('Enter an integer: '))

def number_range(value):
    if 0 <= value <= 50:
        print(f'{value} is between 0 and 50')
    elif 51 <= value <= 100:
        print(f'{value} is between 51 and 100')
    elif value > 100:
        print(f'{value} is greater than 100')
    else:
        print(f'{value} is less than 0')
        
number_range(value)


# The solution given, since there's less to evaluate and easier to read.
# Just go in ascending order to avoid messy conditionals.
# (comment out whichever version you're not testing)

number = int(input('Enter an integer: '))

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')

number_range(number)