# Initialize variables to store sum and count
total = 0
count = 0

# Continually ask the user to enter a number
while True:
    num = input("Enter a number (or -1 to stop): ")

    # Check if the input is -1
    if num == "-1":
        break  # Exit the loop if input is -1
    else:
        # Split the input by "-" and iterate through the individual numbers
        for n in num.split("-"):
            # Attempt to convert each number to float
            try:
                # Add the converted number to the total and increment count
                total += float(n)
                count += 1
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Calculate the average (if count is not 0 to avoid division by zero)
if count != 0:
    average = total / count
    print("Average of the numbers entered (excluding -1):", average)
else:
    print("No numbers entered.")