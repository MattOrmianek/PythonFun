import time
import sys

def another_thing_printing_function(start: int, end: int) -> str:
    # Function for presenting how to print with \r symbol to overwrite the line
    if start > end:
        return "Start must be less than end"
    for i in range(start, end):
        time.sleep(0.1)
        print(f"Było przetesstowanych kluczy: {i}",end='\r')
    return "Koniec testu"

def main() -> None:
    print(another_thing_printing_function(0, 100))

if __name__ == "__main__":
    main()