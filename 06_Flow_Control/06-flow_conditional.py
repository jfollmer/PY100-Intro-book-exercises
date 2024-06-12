value = int(input('Enter a number: '))

# version 1 (comment out whichever versions you're not testing):

if value == 3:
    print('value is 3')

# version 2 (add else statement):

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# version 3 (use elif; does the same thing as v.2):

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')

# version 4 (if statement blocks can have as many lines as you need):

if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')

# version 5 (use pass for readability):

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # we don't care about 9
else:
    print('value is something else')