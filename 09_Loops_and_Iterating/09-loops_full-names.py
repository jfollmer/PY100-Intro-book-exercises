# Loops and Iterating chapter, Simultaneous Iteration section:

# Can use a while loop to iterate through multiple collections simultaneously,
# but error-prone and often messy.

# Suppose you need to print the full names of several thousand people. For 
# bizarre historical reasons, you have two lists: one contains the forenames, 
# and the other contains the corresponding surnames. Without zip, you need to 
# use a while loop and indexing:

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0                       # Create index counter.
while index < len(forenames):   # Use index counter in while loop.
    if index >= len(surnames):  # Surnames might be shorter (could you not just
        break                   # use strict=True? Would produce an instead.
                                # What about != instead of >= ?).
    forename = forenames[index] # Create variable to use in print statement.
    surname = surnames[index]   # Create variable to use in print statement.
    print(f'{forename} {surname}') # Print list of full names from these lists.
    index += 1                  # Increase counter.
# This prints:
# Ken Camp
# Lynn Blake
# Pat Flanagan
# Nancy Short


# zip() is easier:

# forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
# surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames) # Create zipped iterator.
for forename, surname in zipped_names:  # Tuple unpacking in for loop.
# for can assign multiple variables when collection elements are tuples.
    print(f'{forename} {surname}')      # Print list of full names.

# My twist: could rewrite lines 34-35 as one line if you don't need to save it:

# forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
# surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

for forename, surname in zip(forenames, surnames):
    print(f'{forename} {surname}')