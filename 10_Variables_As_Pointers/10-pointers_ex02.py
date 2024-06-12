# Variables as Pointers chapter, exercise 2:

# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# Don't worry about having an exact match for the output. The important part is 
# to show something that accurately represents set2.


# This prints a set with the following set with the values in random order:
# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}
# When set1 is modified on line 7, set2 also reflects this change because 
# on line 6, the same object referenced by the variable set1 is assigned to the 
# variable set2.