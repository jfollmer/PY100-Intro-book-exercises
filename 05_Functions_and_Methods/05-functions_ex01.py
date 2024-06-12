# Functions and Methods chapter, exercise 1:
# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)


# Line 7 calls set_foo, which defines a local variable foo, which is then
# erased again once set_foo is finished executing. print(foo) on line 8 raises
# an error, since there is no global variable foo.