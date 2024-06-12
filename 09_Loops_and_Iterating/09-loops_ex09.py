# Loops and Iterating chapter, exercise 9:

# Don't let the math scare you. This is a logic and syntax problem, not a math 
# problem.

# Write a function that computes and returns the factorial of a number by using 
# a for or while loop. The factorial of a positive integer n, signified by n!, 
# is defined as the product of all ns between 1 and n, inclusive:

# n!	Expansion	        Result
# --    ---------           ------
# 1!	1	                1
# 2!	1 * 2	            2
# 3!	1 * 2 * 3	        6
# 4!	1 * 2 * 3 * 4	    24
# 5!	1 * 2 * 3 * 4 * 5	120

# You may assume that the argument is always a positive n.

# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000


def factorial(n):
    result = n
    while n > 1:
        result = result * (n - 1) # 5, 5*4=20, 20*3=60, 60*2=120
        n -= 1
    return result

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000


# Given solution using a while loop:

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -=1
    return result

# Given solution using a for loop and decreasing range:

def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number
    return result

# Given solution in video using a for loop and increasing range:

def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result