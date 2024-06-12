# Using Collections chapter, exercise 15:

# Without running the following code, what values will be printed by line 10?
# (the final line, line 15 here)

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# Prints dict_keys(['Cat', 'Bird', 'Snake']) because changes to a dictionary
# are immediately reflected in dictionary view objects.