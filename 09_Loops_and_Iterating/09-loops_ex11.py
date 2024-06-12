# Loops and Iterating chapter, exercise 11:

# Challenging Problem: Don't feel bad if you struggle with this problem or 
# can't solve it. The problem is not easy. It is designed to demonstrate why 
# we prefer to use for loops when we can, and a big part of that problem is 
# messy code that is difficult to write and understand. See how far you can 
# get, but don't spend much time struggling.

# Print all of the even numbers in the following list of nested lists. This 
# time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

# Expected output:

# 6
# 4
# 2
# 4
# 16
# 0

outer_index = 0
inner_index = 0
while outer_index < len(my_list):
    while inner_index < (len(my_list[outer_index])):
        if my_list[outer_index][inner_index] % 2 == 0:
            print(my_list[outer_index][inner_index])
        inner_index += 1
    inner_index = 0
    outer_index += 1

# Given solution has inner_index = 0 on a different line and uses a couple
# extra variables:

outer_index = 0
while outer_index < len(my_list):
    inner_list = my_list[outer_index]       # extra variable for readability
    inner_index = 0                         # better line to have this on
    while inner_index < len(inner_list):
        number = inner_list[inner_index]    # extra variable for readability
        if number % 2 == 0:
            print(number)
        inner_index += 1
    outer_index += 1

# a for loop version I wrote for fun:

for l in my_list:       # you can assign the extra variable within a for loop
                        # literal, and no indices needed since a for loop
                        # automatically iterates
    for i in l:
        if i % 2 == 0:
            print(i)