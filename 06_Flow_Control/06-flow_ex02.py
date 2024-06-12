# Flow Control chapter, exercise 2:
# Write Write a function, even_or_odd, that determines whether its argument is 
# an even or odd number. If it's even, the function should print 'even';
# otherwise, it should print 'odd'. Assume the argument is always an integer.

integer = int(input("Input an integer: "))

def even_or_odd(integer):
    if integer % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd(integer)

# alternatively: (comment out whichever version you're not testing)

integer = int(input("Input an integer: "))

print('even' if integer % 2 == 0 else 'odd')