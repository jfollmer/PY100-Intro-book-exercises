# Introduction to Collections chapter, exercise 8:

# How would you print all the numbers in the following range?

# range(3, 17, 4)


# My solution:

my_range = range(3, 17, 4)
for i in range(3, 17, 4):
    print(i)

# or:

print(list(range(3, 17, 4))) # also a given solution


# Another given solution:

print(tuple(range(3, 17, 4)))