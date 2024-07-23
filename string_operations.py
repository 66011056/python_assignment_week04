def reverse_string(s):
    "Reverse a given string."
    return s[::-1]

def capitalize_string(s):
    "Capitalize the first letter of a given string."
    return s.capitalize()

def lowercase_string(s):
    "Convert all characters in a given string to lowercase."
    return s.lower()

def uppercase_string(s):
    "Convert all characters in a given string to uppercase."
    return s.upper()

# Importing the string_operations module
import string_operations as so

# Sample strings and printing results
sample_string = "hello World"

print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string))
