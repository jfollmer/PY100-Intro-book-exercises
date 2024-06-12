# Functions and Methods chapter, exercise 13:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# Raises a syntax error. Once you define a default value for a parameter, all
# subsequent parameters must be defined with default values. Only the second
# parameter is given a default value, but the third is not.