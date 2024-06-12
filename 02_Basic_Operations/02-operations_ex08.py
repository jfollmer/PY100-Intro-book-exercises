# Basic Operations chapter, exercise 8:
# To what value does the following expression evaluate?

'12' < '9'


# True, because looking at the first element in each string,
# the *character* (not the integer) '1' is < '9'. The '2' is not
# evaluated, since iterable objects are evaluated left-to-right, and
# Python stops evaluating once it finds the first difference.