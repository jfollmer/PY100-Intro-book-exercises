# Functions and Methods chapter, exercise 7:
# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# Raises an error, since the function foo on line 7 requires 2 arguments, no
# default parameter values are defined, and the function call on line 8 only
# passes one argument.