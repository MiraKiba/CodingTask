# Define the number of rows in the pattern
rows = 5

# Iterate through each row
for i in range(1, 2 * rows):
    # Calculate the number of stars to print in each row
    if i <= rows:
        stars = i
    else:
        stars = 2 * rows - i

    # Print the stars for the current row
    print("*" * stars)