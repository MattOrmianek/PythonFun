from app import loop_function

#acythonize
def hello_world():
    return "hello_world"

#acythonize
def math_calc(num1, num2):
    return num1 * num2

#acythonize
def multipy_string(text):
    return text * 10

# this is for testing only
def test():
    return "test"

def main():
    hello_world()
    print(math_calc(2,3))

if __name__ == "__main__":
    main()