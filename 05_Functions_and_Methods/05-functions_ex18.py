# Functions and Methods chapter, exercise 18:
# The following function returns a list of the remainders of dividing the 
# numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at 
# least one number that is not evenly divisible by 3 (that is, the remainder 
# is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

# My answer:

def divisible_by_3(numbers):
    remainders = remainders_3(numbers)
    for r in remainders:
        if r > 0:
            print('Contains numbers not divisible by 3')
            return
    print('Does not contain numbers not divisible by 3')

divisible_by_3(numbers_1)   # Contains numbers not divisible by 3
divisible_by_3(numbers_2)   # Contains numbers not divisible by 3
divisible_by_3(numbers_3)   # Does not contain numbers not divisible by 3
divisible_by_3(numbers_4)   # Does not contain numbers not divisible by 3

# Given solution:

print(any(remainders_3(numbers_1)))    # True
print(any(remainders_3(numbers_2)))    # True
print(any(remainders_3(numbers_3)))    # False
print(any(remainders_3(numbers_4)))    # False

# any() returns True if any values are truthy, false if none are truthy