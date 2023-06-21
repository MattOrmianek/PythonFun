# Automate cythonize code
import sys
import re
# take first argument as file in which look for automate cythonize
file = sys.argv[1]

print(f"Automate cythonize process on {file} file.")


# open file
with open(file, 'r') as file:
    text = file.read()

#print(f"content_of_file: \n {text}")

word = '#acythonize'
words = text
words = text.split()
matches = []
for index, w in enumerate(words):
    if w == word.lower():
        matches.append(index)

print(f"The word '{word}' appears {len(matches)} times in the string.")
for match in matches:
    print(f"Found at position {match}: '{words[match]}'")
