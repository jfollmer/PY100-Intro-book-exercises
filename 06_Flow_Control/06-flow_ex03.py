# Flow Control chapter, exercise 3:
# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # Prints 'Product2' because it matches the second case.

bar_code_scanner(142) # Prints 'Product not found!' because 142 the third case
# compares the argument with a string, not an integer, so the default case
# is executed.