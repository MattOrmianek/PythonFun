from app import loop_function

#acythonize
def hello_world():
    return "hello_world"

#acythonize
def math_calc(num1, num2):
    return num1 * num2


def main():
    hello_world()
    print(math_calc(2,3))

if __name__ == "__main__":
    main()