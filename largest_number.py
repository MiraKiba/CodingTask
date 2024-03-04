def largest_number(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = largest_number(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest

# Testing the function
print(largest_number([1, 4, 5, 3]))                 # Output should be 5
print(largest_number([3, 1, 6, 8, 2, 4, 5]))       # Output should be 8