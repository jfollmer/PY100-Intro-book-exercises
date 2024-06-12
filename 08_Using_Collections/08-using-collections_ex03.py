# Using Collections chapter, exercise 3:

# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple 
# should be in reverse order from the original. It should also exclude the 
# first and last members of the original. The result should be the tuple 
# (4, 3, 2).


# My solution:

my_tuple = (1, 2, 3, 4, 5)
new_tuple = []
for item in reversed(my_tuple[1:4]):
    new_tuple.append(item)
new_tuple = tuple(new_tuple)
print(new_tuple)    # (4, 3, 2)


# Given solution 1:

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)       # (4, 3, 2)

# Given solution 2:

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       # (4, 3, 2)

# Given solution 3:

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)