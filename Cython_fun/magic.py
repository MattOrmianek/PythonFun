# USE: python3 magic.py <file>
# Automate cythonize code
import sys
import re
# Plan:
# Fix problem with random_choice function, it only takes first return and skips another one
# Write tests for already existing code
# Write error catching
# Check how to edit string and save it properly with indentation
# Make list of rules how to change python code to cython code
# Make list of types variables and how they change for cython

try:
    file = sys.argv[1]
    print(f"Automate cythonize process on {file} file.")
except Exception as e:
    print(f"Error: {e}")
    print("Can't open file")


def find_function_end(text, start_line):
    if text != "":
        code_lines = text.strip().split("\n")
        try:
            indent = code_lines[start_line].split()[0]
        except Exception as e:
            print(f"Error: {e}")
            return "There are not that many lines"
    else:
        return "No text"

    end_line = start_line

    for line_number in range(start_line + 1, len(code_lines)):
        line = code_lines[line_number]
        if line.startswith("def"):
            break

        if line.startswith(indent):
            end_line = line_number

        if "return" in line:
            end_line = line_number

    return end_line


def magic(file):
    with open(file, "r") as file:
        text = file.read()

    word = "#acythonize"  # marker in code which code need to be cythonized

    lines = text.splitlines()
    matches = []
    lines_of_function = []
    for line_number, line in enumerate(lines):
        if word.lower() in line.lower():
            matches.append((line_number, line.index(word.lower())))

    for match in matches:
        line_number, position = match
        lines_of_function.append(line_number + 1)

    list_of_functions = []
    for function in lines_of_function:
        function_end_line = find_function_end(text, function)
        function_content = "\n".join(lines[function : function_end_line + 1])

        print(
            f"\nThe functions starts at {function} and ends at {function_end_line + 1}"
        )
        print(f"Function code: \n {function_content}")
        list_of_functions.append(function_content)

    return list_of_functions


def convert_to_cython(function: str):
    # list of rules
    # 1. change def to cpdef
    # 2. add definition of type of variables - get the variables - check the type (somehow)
    function = function.replace("def", "cpdef")
    list_of_variables = []
    matches = re.findall(r"\((.*?)\)", function)
    for variable in matches:
        if variable == "":
            variable = None
        list_of_variables.append(variable)

    print(f"variables: {list_of_variables}")
    print(f"function:\n {function} \n")
    return 0


def main():
    list_of_functions = magic(file)
    # for function in list_of_functions:
    #    convert_to_cython(function)


if __name__ == "__main__":
    main()
