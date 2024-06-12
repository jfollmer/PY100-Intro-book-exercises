# Functions and Methods chapter, exercise 2:
# What does this program print? Why?

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)


# A global variable foo is defined. set_foo then defines a local variable also
# named foo, which prevents the function from using the global variable foo
# (variable shadowing). The local variable foo is then erased again once the 
# function finishes. Line 10 prints 'bar', since the global variable foo is
# unaffected.