# Basic Operations chapter, exercise 2:

# This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.
#
# Use the REPL and the arithmetic operators to extract the individual digits of 4936:
#
# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.


number = 4936
print("Ones place: ", number % 10)
print("Tens place: ", number // 10 % 10)
print("Hundreds place: ", number // 100 % 10)
print("Thousands place: ", number // 1000)