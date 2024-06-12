# More Stuff chapter, exercise 1:

# What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()
    # sorted dictionary keys:
    # ['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor']
    # returns CHRIS (from index 1, in uppercase)

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))    # prints CHRIS