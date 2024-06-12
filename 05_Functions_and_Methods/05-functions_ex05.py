# Functions and Methods chapter, exercise 5:
# What does the following code print?

def scream(words):
    return words + '!!!!'   # returns 'Yipeee!!!!'

scream('Yipeee')            # does nothing with the return value

# Prints nothing. 'Yipeee' is passed to scream on line 7. The function
# scream defined on lines 4-5 then concatenates this string with a string of
# exclamation points, which is then returned. However, the function call on
# line 7 should have been passed as an argument to print in order to print the
# return value of scream ('Yipeee!!!!'), and it wasn't, so nothing prints.