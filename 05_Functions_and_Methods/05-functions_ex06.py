# Functions and Methods chapter, exercise 6:
# What does the following code print?

def scream(words):
    words = words + '!!!!'  # words = 'Yipeee!!!!'
    return                  # returns None
    print(words)            # not executed

scream('Yipeee')            # does nothing with return value

# Nothing is printed. The function called on line 9 returns None on line 6,
# and the print statement on line 7 is not executed. There are no other print
# statements.