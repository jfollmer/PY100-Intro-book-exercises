# Variables chapter, exercise 10:
# Assume that obj already has a value of 42 when the code below starts running.
# Which of the subsequent statements reassign the variable? Which statements 
# mutate the value of the object that obj references? Which statements do 
# neither? If necessary, you can read the documentation.

obj = 42            # original value

obj = 'ABcd'        # reassignment
obj.upper()         # neither, returns a new string 'ABCD', "doesn't mutate the 
                    # caller" and "haven't done anythin to capture the return
                    # value" phrasings in given solution
obj = obj.lower()   # reassignment to 'abcd'
print(len(obj))     # neither, prints 4, "doesn't mutate its argument" and 
                    # "not a mutating function" phrasings in given solution
obj = list(obj)     # reassignment to ['a', 'b', 'c', 'd']
obj.pop()           # mutation, now obj = ['a', 'b', 'c'], returns 'X'
obj[2] = 'X'        # mutation, now obj = ['a', 'b', 'X']
obj.sort()          # mutation, now obj = ['X', 'a', 'b']
set(obj)            # neither, returns a new set {'X', 'a', 'b'} (any order)
obj = tuple(obj)    # reassignment to ('X', 'a', 'b')