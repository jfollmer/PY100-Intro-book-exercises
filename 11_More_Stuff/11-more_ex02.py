# More Stuff chapter, exercise 2:

# Use the sqrt function from the math library to write some code that outputs 
# the square root of 37. Try to write the code in three different ways.


import math

# Version 1:

print(math.sqrt(37))

# Version 2:

import math

number = 37
print(math.sqrt(number))

# Version 3:

import math as m

print(m.sqrt(37))

# Version 4:

import math as m

number = 37
print(m.sqrt(number))

# Version 5:

import math

numbers = [37]
for number in numbers:
    print(math.sqrt(number))


# Given solution uses yet another different import statement, didn't realize
# that was the specific statement being asked to be different:

from math import sqrt

print(sqrt(37))