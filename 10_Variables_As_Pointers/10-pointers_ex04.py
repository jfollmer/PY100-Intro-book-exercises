# Variables as Pointers chapter, exercise 4:

# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])


# This prints [1, 42, 3]. On line 10, we pass dict1 to the dict() constructor,
# which creates a new shallow copy of the dictionary referenced by dict1.
# Since shallow copies only contain references to nested objects, the list and
# tuple objects assigned to the keys in these dictionaries will be shared by
# both copies of the dictionary, even though the dictionaries themselves are
# two separate objects. So when we modify the list object assigned to 'a' in 
# dict1 on line 11, this change is reflected when printing the value of 'a' in
# dict2 on line 12.