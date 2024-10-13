# Reverse a string

example_string = "This is example string"

def reverse_string(s: str) -> str:
    return s[::-1]

assert reverse_string(example_string) == "gnirts elpmaxe si sihT"
