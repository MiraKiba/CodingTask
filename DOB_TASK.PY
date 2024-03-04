# Read the content of the file "DOB.txt"
with open("DOB.txt", "r") as file:
    data = file.read()

# Split the content of the file into separate lines
lines = data.split("\n")

# Iterate over each line to separate names and dates
for line in lines:
    # Split each line into name and date using comma as a delimiter
    name, date = line.split(",")

    # Print the name and date separately
    print("Name:", name)
    print("Date:", date)