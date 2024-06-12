# Using Collections chapter, exercise 13:

# Without running the following code, determine what each print statement 
# should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)       # True ('Butterscotch' is an element in 
                                    # cats)
print('Butter' in cats)             # False ('Butter' is not an element in 
                                    # cats)
print('Butter' in cats[3])          # True ('Butter' is a substring of 
                                    # 'Butterscotch')
print('cheddar' in cats)            # False (case doesn't match)