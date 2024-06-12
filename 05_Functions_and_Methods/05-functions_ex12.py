# Functions and Methods chapter, exercise 12:
# Without running the followung code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# Raises an error, since foo takes 3 arguments, only the second two parameters 
# parameters are defined with default values, and no arguments were passed on
# line 9. foo requires at least one argument to be passed.