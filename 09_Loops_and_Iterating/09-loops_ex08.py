# Loops and Iterating chapter, exercise 8:

# Write a comprehension that creates a dict object whose keys are strings and 
# whose values are the length of the corresponding key. Only keys with odd 
# lengths should be in the dict. Use the set given by my_set as the source of 
# strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}


# My solution:

my_dict = { name: len(name) 
            for name in my_set 
            if len(name) % 2 == 1 }
print(my_dict)