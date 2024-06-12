# Using Collections chapter, exercise 2:

# Use slicing to write Python code to print a 6-character substring of 
# 'Launch School' that begins with the first c.


# My solution:

my_string = 'Launch School'
print(my_string[4:10])  # ch Sch


# Another given solution (more prgrammatic):

my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start:start + 6])  # ch Sch