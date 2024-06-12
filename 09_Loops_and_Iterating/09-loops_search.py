# This continues to iterate after it finds the value:

numbers = [3, 1, 5, 9, 2, 6, 4, 7]  # List you're searching through.
found_item = -1                     # Item you're looking for.
                                    # Why is this -1? To equal False?
index = 0                   # Counter matching index for the while loop to use.

while index < len(numbers): # While loop uses counter to iterate thru indices.
    if numbers[index] == 5:         # If current index is value searched for:
        found_item = index          # Store index location.
    index += 1                      # Increase counter.
print(found_item)                   # Finally print index where value found.


# Use break to stop iterating after the value is found:

numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers): # While loop uses counter to iterate thru indices.
    if numbers[index] == 5:         # If current index is value searched for:
        found_item = index          # Store index location.
        break                       # Break the loop/stop searching once found
                                    # (this is within an if statement, not a
                                    # nested loop, so breaks the 'outer' loop)
    index += 1                      # Increase counter.
print(found_item)                   # Finally print index where value found.