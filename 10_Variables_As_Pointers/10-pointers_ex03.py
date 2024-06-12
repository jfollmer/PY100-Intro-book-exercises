# Variables as Pointers chapter, exercise 3:

# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])


# On line 11, the dict() constructor creates an entirely new dictionary based 
# on the dictionary assigned to dict1, and that is assigned to dict2. So when 
# we modify dict2 on line 12, this does not affect the dictionary assigned to 
# dict1. Therefore, when we access the 'Monty Python' key on line 13, this 
# prints 'The Life of Brian'

# If we had put dict2 = dict1 on line 11, the value would have been reflected
# by both variables.

# Given solution also mentions that the dict() constructor creates a shallow
# copy, so any nested objects would be shared by both dictionaries.