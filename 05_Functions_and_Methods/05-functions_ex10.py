# Functions and Methods chapter, exercise 10:
# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)        # 42 (first argument passed)
    print(second)       # 3.141592 (second argument passed)
    print(third)        # 2 (default value)

foo(42, 3.141592)

# Prints 42, 3.141592, and 2 on separate lines. The first two values are passed
# to foo on line 9. Foo can take 3 arguments, but default values are defined
# for the second and third parameters. The default value isn't used for the 
# second one since it's been passed, but the third is used since only two 
# arguments were passed.