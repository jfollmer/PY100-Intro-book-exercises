# Loops and Iterating chapter, exercise 2:

# Modify the age.py program you wrote in Exercise 3 of the Input/Output 
# chapter. The updated code should use a for loop to display the future ages.


# Previous program:

# age = int(input("How old are you? "))

# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')


# Revised solution:

age = int(input("How old are you? "))

def future_ages(age):
    print(f'You are {age} years old.')
    for i in range(10, 50, 10):
        print(f'In {i} years, you will be {age + i} years old.')

future_ages(age)