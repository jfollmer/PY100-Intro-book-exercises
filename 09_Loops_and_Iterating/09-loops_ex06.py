# Loops and Iterating chapter, exercise 6:

# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this 
# problem, you should write code that creates a new list with one element for 
# each number in my_list. If the original number is an even, then the 
# corresponding element in the new list should contain the string 'even'; 
# otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# Expected output:
# pretty-printed for clarity
[
    'odd', 'odd', 'even', 'odd',
    'even', 'even', 'even', 'odd',
    'odd', 'even', 'even'
]


new_list = []
for number in my_list:
    if number % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')
print(new_list)


# Alternate given solution using a list comprehension:

result = [ 'even' if number % 2 == 0 else 'odd'
            for number in my_list ] # list comprehension
print(result)

# Alternate given solution using a helper function with a ternary expression,
# and a list comprehension:

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd' # ternary expression

result = [ odd_or_even(number)
           for number in my_list ] # list comprehension
print(result)

# Good use case for comprehensions bc you're creating a new list with the same 
# number of elements, and each element in the new list is based upon the 
# corresponding element from the original list. In other words, transforming.