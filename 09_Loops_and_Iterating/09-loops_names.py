# Loops and Iterating chapter, example in while Loops and for Loops sections:


# WHILE LOOP VERSION:

names = ['Chris', 'Max', 'Karis', 'Victor']     # Original list.
upper_names = []                                # New list.
index = 0                                       # Counter that matches indices.
# Initialize these outside the loop, or they'd get reset every iteration.

while index < len(names):                   # Use counter in condition.
    upper_name = names[index].upper()       # New temporary local variable to
                                            # store the value you're copying.
    upper_names.append(upper_name)
    index += 1                              # Modify the counter *after* each
                                            # iteration.

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

# In other words:

#index = 0
#while index < len(collection):
     # loop body
     # do something with collection[index]
#    index += 1


# FOR LOOP VERSION:

names = ['Chris', 'Max', 'Karis', 'Victor']     # Original list.
upper_names = []                                # New list.

for name in names:                  # Variable name for each element.
    upper_name = name.upper()       # Temporary local variable to store the
                                    # value you're copying.
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

# Result is the same, but this code is easier to read and maintain.
# More elegant, and less error-prone.


# If you want all the names uppercase except 'Max', you could use continue
# (tells Python to start the next iteration of the enclosing loop):

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']


# Can often use a negated if conditional to avoid using continue:

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name != 'Max':
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']

# But using continue is often more elegant than nested conditional logic, e.g.
# you could do this:

for value in collection:
    if some_condition:
        # some code here
        if another_condition:
            # some more code here

# but this is less cluttered:

for value in collection:
    if not some_condition:
        continue
    # some code here
    if not another_condition:
        continue
    # some more code here

# It's subjective as to which is easier to read/maintain/write.