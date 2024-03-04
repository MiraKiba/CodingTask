# Ask the user to enter a sentence
str_manip = input("Please enter a sentence: ")

# Calculate and display the length of str_manip
print("Length of the sentence:", len(str_manip))

# Find the last letter in str_manip
last_letter = str_manip[-1]

# Replace every occurrence of the last letter with '@'
str_manip_modified = str_manip.replace(last_letter, '@')

# Print the modified sentence
print("Modified sentence:", str_manip_modified)

# Print the last 3 characters in str_manip backwards
print("Last 3 characters backwards:", str_manip[-1:-4:-1])

# Create a five-letter word from the first three and last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]

# Print the five-letter word
print("Five-letter word:", five_letter_word)