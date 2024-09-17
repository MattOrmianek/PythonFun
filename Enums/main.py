"""
Enums are used to define a set of named values that are mutually exclusive.
"""

from enum import Enum, Flag, auto


class Color(Enum):
    """
    This is a simple enum with three colors.
    """

    RED: str = "Red"
    GREEN: str = "Green"
    BLUE: str = "Blue"


print(Color.RED)
print(repr(Color.RED))
print(Color.RED.name)
print(Color.RED.value)

print(Color.GREEN)
print(repr(Color.GREEN))
print(Color.GREEN.name)
print(Color.GREEN.value)


def create_car(color: Color) -> None:
    """
    This function creates a car with a given color.
    """
    print(f"Creating a car with color: {color}")
    match color:
        case Color.RED:
            print("The car is red")
        case Color.GREEN:
            print("The car is green")
        case Color.BLUE:
            print("The car is blue")
        case _:
            print("The car is unknown")


create_car(Color.RED)
create_car(Color.GREEN)
create_car(Color.BLUE)


class ColorFlag(Flag):
    """
    This is a simple flag enum with five colors.
    """

    RED: int = 1
    GREEN: int = 2
    BLUE: int = 4
    YELLOW: int = 8
    PURPLE: int = 16


yellow_and_blue = ColorFlag.YELLOW | ColorFlag.BLUE
print(yellow_and_blue)
print(ColorFlag.YELLOW in yellow_and_blue)
print(ColorFlag.RED in yellow_and_blue)


class ColorFlagAuto(Flag):
    """
    This is a simple flag enum with five colors.
    """

    RED: int = auto()
    GREEN: int = auto()
    BLUE: int = auto()
    YELLOW: int = auto()
    PURPLE: int = auto()


print(ColorFlagAuto.RED)
print(ColorFlagAuto.GREEN)
print(ColorFlagAuto.BLUE)
combination = ColorFlagAuto.RED | ColorFlagAuto.GREEN
print(combination)
print(ColorFlagAuto.RED in combination)
