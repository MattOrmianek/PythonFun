# Automate cythonize code
import sys
import re
# take first argument as file in which look for automate cythonize
file = sys.argv[1]

print(f"Automate cythonize process on {file} file.")






def find_function_end(text, start_line):

    code_lines = text.strip().split('\n')
    indent = code_lines[start_line].split()[0]  # Get the indentation of the starting line
    end_line = start_line

    for line_number in range(start_line + 1, len(code_lines)):
        line = code_lines[line_number]

        # Check if the line is indented with the same indentation as the starting line
        if line.startswith(indent):
            end_line = line_number  # Update the end line

        # Check if the line contains a 'return' statement
        if 'return' in line:
            end_line = line_number  # Update the end line
            break  # Exit the loop

    return end_line





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


lines_of_function = []
for match in matches:
    line_number, position = match
    print(f"Found at line {line_number + 1}, position {position}: '{lines[line_number]}'")
    lines_of_function.append(line_number+1)


for function in lines_of_function:
    function_end_line = find_function_end(text, function)

    print(f"The functions starts at {function} and ends at {function_end_line+1}")

    print("Function code:")
    print('\n'.join(lines[function:function_end_line+1]))