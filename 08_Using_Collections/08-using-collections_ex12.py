# Using Collections chapter, exercise 12:

# Write some code that determines and prints whether the number 3 appears 
# inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# You should print True or False depending on each result.


# My first solution:

def find_3(numbers):
    result = False
    for number in numbers:
        if number == 3:
            result = True
    print(result)

find_3(numbers1)
find_3(numbers2)
find_3(numbers3)
find_3(numbers4)
find_3(numbers5)

# My alternate solution:

def find_3(numbers):
    if 3 in numbers:
        print(True)
    else:
        print(False)

find_3(numbers1)
find_3(numbers2)
find_3(numbers3)
find_3(numbers4)
find_3(numbers5)

# Given solution:

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)        # in is basically ==, so 3.0 == 3