# Loops and Iterating chapter, exercise 7:

# Write a find_integers function that returns a list of all the integers from 
# my_tuple:

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

# Note: You can use the expression type(object) is int to determine whether an 
# object is an integer. For instance:

# print(type(True) is int)      # False (boolean)
# print(type([1, 2, 3]) is int) # False (list)
# print(type(3.141592) is int)  # False (float)
# print(type(77) is int)        # True

# You may receive a SyntaxWarning warning message from the last two examples. 
# You can ignore that warning.

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(iterable):
    integers = []
    for item in iterable:
        if type(item) is int:
            integers.append(item)
    return integers

integers = find_integers(my_tuple)
print(integers)

# Given solution uses a comprehension, so here's my alternate version using a 
# comprehension:

def find_integers(iterable):
    integers = [ item for item in iterable if type(item) is int ]
    return integers

integers = find_integers(my_tuple)
print(integers)

# When you have a pattern of creating an empty list, pushing some things into
# it from another collection, and returning that list, that's often a good use
# case for a comprehension, since list comprehensions are automatically  
# populating a new list with some elements (sometimes transformed) of an 
# existing collection.