# Functions and Methods chapter, exercise 11:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)        # 42
    print(second)       # 3
    print(third)        # 2

foo(42)

# Prints 42, 3, and 2 on separate lines. Only one argument is passed to foo on
# line 9, and foo is defined with default values for the second and third 
# parameters, so these are used since no second or third arguments were passed.