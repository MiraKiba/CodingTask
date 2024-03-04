def alternate_case_characters(input_string):
    result = ''
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(input_string):
    words = input_string.split()
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

# Test alternate_case_characters
input_string = "Hello World"
result_characters = alternate_case_characters(input_string)
print("Alternate Case Characters:", result_characters)

# Test alternate_case_words
input_string = "I am learning to code"
result_words = alternate_case_words(input_string)
print("Alternate Case Words:", result_words)