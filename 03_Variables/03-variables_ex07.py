# Variables chapter, exercise 7:
# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
# Good Morning, Victor
print('Good Afternoon, ' + NAME)
# Good Afternoon, Victor
print('Good Evening, ' + NAME)
# Good Evening, Victor

NAME = 'Nina'
print('Good Morning, ' + NAME)
# Good Morning, Nina
print('Good Afternoon, ' + NAME)
# Good Afternoon, Nina
print('Good Evening, ' + NAME)
# Good Evening, Nina


# Since NAME is a string in both blocks, the + operator concatenates each of
# these strings with the string preceding it in each print argument.

# NAME looks like it's supposed to be a constant, but it was reassigned,
# which is technically allowed for constants even though it's against 
# style conventions.