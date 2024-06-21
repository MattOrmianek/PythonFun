""" This is example of a simple cython function complicated with external modules """
from module1 import module1_function
from module2 import module2_function

def main():
    """ Main function """
    print("Hello world")
    print(module1_function())
    print(module2_function())

if __name__ == "__main__":
    main()