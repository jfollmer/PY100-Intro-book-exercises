# version 1:

value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _:                                 # default case
        print('value is neither 5 nor 6')

# ^^ is functionally equivalent to:

value = 5

if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')

# to match multiple values in one case, use | :

value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:                                 # default case
        print('value is not 1, 2, 3, 4, 5, or 6')