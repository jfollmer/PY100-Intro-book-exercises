# Using Collections chapter, exercise 8:

# Explain why the code below prints different values on lines 3 and 4 (lines 9
# and 10 here).

text = "It's probably pining for the fjords!"
#       012345678901234567890123456789012345

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29


# On line 9, text[21:35] evaluates as the slice "for the fjords!" We pass 'f' 
# to the .rfind() method on this slice, which searches right-to-left for the
# first instance of 'f' and returns that index position in that slice, 8,
# to print().

# On line 10, we are using the whole string rather than a slice to call
# .rfind(), and passing in a range of the string to search. The index value
# returned is the index position in the whole string, 29, which is passed to
# print.