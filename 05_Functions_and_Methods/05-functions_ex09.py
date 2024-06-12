# Functions and Methods chapter, exercise 9:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# Prints 42, 3.141592, and 2.718 on separate lines. All three numbers are
# passed as arguments to foo on line 9, so the default values of the parameters
# are not used. The print statements in the function body print value in order.