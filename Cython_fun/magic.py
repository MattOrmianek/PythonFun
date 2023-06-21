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

lines = text.splitlines()
matches = []
for line_number, line in enumerate(lines):
    if word.lower() in line.lower():
        matches.append((line_number, line.index(word.lower())))

# Print the number of occurrences and their positions
print(f"The word '{word}' appears {len(matches)} times in the string.")
for match in matches:
    line_number, position = match
    print(f"Found at line {line_number + 1}, position {position}: '{lines[line_number]}'")