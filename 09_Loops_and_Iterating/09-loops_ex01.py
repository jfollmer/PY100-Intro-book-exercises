# Loops and Iterating chapter, exercise 1:

# The following code causes an infinite loop (a loop that never stops 
# iterating). Why?

counter = 0

while counter < 5:
    print(counter)


# while loops require some piece of code that eventually alters the condition
# so that it's falsy. This function never alters the value of counter, so
# counter will always be < 5. You should add counter += 1 as the last line of 
# the function body.