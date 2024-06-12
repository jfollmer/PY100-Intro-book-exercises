# Introduction to Collections chapter, exercise 2:

# Can you write some code to change the value 'bye' in the following tuple to 
# 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')    # the given code to change

# My solution, building a new list with iteration and reassigning the original
# tuple once that's done:

stuff_list = list()
for word in stuff:
    if word == 'bye':   
        substitution = 'goodbye'
        stuff_list.append(substitution)
    else:
        stuff_list.append(word)
stuff = tuple(stuff_list)
print(stuff)


# Given solution that isn't great since slicing and indexing is vulnerable to 
# off-by-one errors:

stuff = ('hello', 'world', 'bye', 'now')

stuff = stuff[0:2] + ('goodbye', stuff[3])

# A better given solution (convert to a list, make the changes, convert back 
# into a tuple):

stuff = ('hello', 'world', 'bye', 'now')

stuff = list(stuff)
stuff[2] = 'goodbye' # I think this is also prone to off-by-one errors though
stuff = tuple(stuff)


# My modifed solution using index access / element assignment in a way that
# avoids off-by-any error:

stuff = ('hello', 'world', 'bye', 'now')

stuff = list(stuff)
for word in stuff:
    if word == 'bye':
        stuff[stuff.index(word)] = 'goodbye'
stuff = tuple(stuff)
print(stuff)