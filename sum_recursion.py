def adding_up_to(lst, index):
    if index == 0:
        return lst[0]
    else:
        return lst[index] + adding_up_to(lst, index - 1)

# Testing the function
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Output should be 25
print(adding_up_to([4, 3, 1, 5], 1))          # Output should be 7