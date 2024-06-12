# Using Collections chaper, exercise 5:

# Which of the following values can't be used as a key in a dict object, 
# and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']          # can't be used as a key, lists are mutable and nonhashable
{'a': 1, 'b': 2}    # can't be used, dictionaries are mutable and nonhashable
range(5)
{1, 4, 9, 16, 25}   # can't be used, sets are mutable and nonhashable
3
0.0
frozenset({1, 4, 9, 16, 25})