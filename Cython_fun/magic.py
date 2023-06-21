# USE: python3 magic.py <file>
# Automate cythonize code
import sys
import re
# Plan:
# Make all in functions
# Write tests for already existing code
# Write error catching
# Check how to edit string and save it properly with indentation
# Make list of rules how to change python code to cython code
# Make list of types variables and how they change for cython

file = sys.argv[1]
print(f"Automate cythonize process on {file} file.")

def find_function_end(text, start_line):

    code_lines = text.strip().split('\n')
    indent = code_lines[start_line].split()[0]
    end_line = start_line

    for line_number in range(start_line + 1, len(code_lines)):
        line = code_lines[line_number]

        if line.startswith(indent):
            end_line = line_number

        if 'return' in line:
            end_line = line_number
            break

    return end_line

def magic(file):
    # open file
    with open(file, 'r') as file:
        text = file.read()

    word = '#acythonize' # marker in code which code need to be cythonized

    lines = text.splitlines()
    matches = []
    for line_number, line in enumerate(lines):
        if word.lower() in line.lower():
            matches.append((line_number, line.index(word.lower())))

    lines_of_function = []
    for match in matches:
        line_number, position = match
        lines_of_function.append(line_number+1)

    for function in lines_of_function:
        function_end_line = find_function_end(text, function)

        print(f"The functions starts at {function} and ends at {function_end_line+1}")
        print("Function code:")
        print('\n'.join(lines[function:function_end_line+1]))

def main():
    magic(file)

if __name__ == "__main__":
    main()