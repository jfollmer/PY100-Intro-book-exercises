# Loops and Iterating chapter, exercise 3:

# Use a while loop to print the numbers in my_list, one number per line. Then, 
# do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected output:

# 6
# 3
# 0
# 11
# 20
# 4
# 17


# Comment out whichever block you're not testing:

# while loop:

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# for loop:

for number in my_list:
    print(number)