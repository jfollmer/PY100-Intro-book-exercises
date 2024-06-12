# Flow Control chapter, exercise 5:
# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:     # equivalent to if my_list == True:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])   # Prints 'Empty' because an empty collection is falsy,
                    # so the else block is executed.