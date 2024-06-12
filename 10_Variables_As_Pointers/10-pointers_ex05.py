# Variables as Pointers chapter, exercise 5:

# Write some code to create a deep copy of the dict1 object and assign it to 
# dict2. You should only modify the code where indicated.

# You may modify this line
import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

# dict2 = ??? # You may modify the `???` part of this line
dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1         is dict2)           # whole dictionaries
print(dict1['a']    is dict2['a'])      # [[7, 1], ['aa', 'aaa']]
print(dict1['a'][0] is dict2['a'][0])   # [7, 1]
print(dict1['a'][1] is dict2['a'][1])   # ['aa', 'aaa']
print(dict1['b']    is dict2['b'])      # ([3, 2], ['bb', 'bbb])
print(dict1['b'][0] is dict2['b'][0])   # [3, 2]
print(dict1['b'][1] is dict2['b'][1])   # ['bb', 'bbb]

# All of these should print True
print(dict1['a'][0][0] is dict2['a'][0][0]) # 7 is an integer, immutable
print(dict1['a'][0][1] is dict2['a'][0][1]) # 1 is an integer, immutable
print(dict1['a'][1][0] is dict2['a'][1][0]) # 'aa' is a string, immutable
print(dict1['a'][1][1] is dict2['a'][1][1]) # 'aaa' is a string, immutable
print(dict1['b'][0][0] is dict2['b'][0][0]) # 3 is an integer, immutable
print(dict1['b'][0][1] is dict2['b'][0][1]) # 2 is an integer, immutable
print(dict1['b'][1][0] is dict2['b'][1][0]) # 'bb' is a string, immutable
print(dict1['b'][1][1] is dict2['b'][1][1]) # 'bbb' is a string, immutable