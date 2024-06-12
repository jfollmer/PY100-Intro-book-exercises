# Functions and Methods chapter: Exercise 19

# Use the remainders_5 function to determine which of the following lists
# do NOT contain numbers divisible by 5.

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # False (some by 5 (the 0s))
          # [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0]   # all() returns False

numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]            # True (none by 5 (none are 0))
          # [1, 2, 3, 4, 1, 2, 3, 4]            # all() returns True
          
numbers_3 = [0, 5, 10]                          # False (some by 5 (the 0s))
          # [0, 0, 0]                           # all() returns False
          
numbers_4 = []                                  # True (none by 5)
          # []                                  # all() returns True

# My answer:

def none_divisible_by_5(numbers):
    if all(remainders_5(numbers)):
        return "True. Does not contain any numbers divisible by 5."
    else:
        return "False. Contains at least 1 number divisible by 5."

print(none_divisible_by_5(numbers_1))
print(none_divisible_by_5(numbers_2))
print(none_divisible_by_5(numbers_3))
print(none_divisible_by_5(numbers_4))

# Given solution:

print(all(remainders_5(numbers_1)))    # False
print(all(remainders_5(numbers_2)))    # True
print(all(remainders_5(numbers_3)))    # False
print(all(remainders_5(numbers_4)))    # True

# all() returns True if no values are falsy
# (includes empty sets since none are falsy)