# Functions and Methods chapter, exercise 8:
# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# Raises an error, since 3 arguments are passed to foo on line 8, but foo only
# takes two arguments.