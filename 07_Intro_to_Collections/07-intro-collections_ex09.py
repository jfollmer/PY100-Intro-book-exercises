# Introduction to Collections chapter, exercise 9:

my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your 
# answers:
# 1. Are the lists assigned to my_list and another_list equal?
# 2. Are the lists assigned to my_list and another_list the same object?
# 3. Are the nested lists at index 3 of my_list and another_list equal?
# 4. Are the nested lists at index 3 of my_list and another_list the same 
#    object?
# Don't write any code for this exercise.


# 1. Yes. On line 4 the list() constructor creates a shallow copy of my_list, 
#    which is assigned to another_list. These two lists are equal since they
#    contain the same values.
# 2. No, they are shallow copies, as explained in answer 1, which are separate
#    objects.
# 3. Yes, a shallow copy of a nested list is actually just a copy of the 
#    pointer to the same list object, so they are equal.
# 4. Yes, as explained in answer 3, they are the same object