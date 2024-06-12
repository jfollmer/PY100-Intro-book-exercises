# Variables as Pointers chapter, exercise 1:

# In your own words, explain the difference between these two expressions.

my_object1 == my_object2
my_object1 is my_object2

# Line 5 evaluates whether the object referenced by my_object1 is equivalent to
# the object referenced by my_object2.
# Line 6 evaluates whether the object reference by my_object1 is the same 
# object as the the one referenced by my_object2. Essentially it compares 
# id(my_object1) == id(my_object2).

# Given solution uses the terms value equality vs. object equality.