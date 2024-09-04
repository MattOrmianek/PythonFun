""" This is checking OOP and dunder methods """


class Microwave:
    """Microwave class for creating new microwaves"""

    def __init__(self, brand: str, power: str) -> None:
        self.brand = brand
        self.power = power
        self.status: bool = False

    def turn_on(self) -> None:
        """Function for turning on microwave"""
        if self.status:
            print("Microwave already turned on")
        else:
            self.status = True

    def turn_off(self) -> None:
        """Function for turning off microwave"""
        if self.status:
            self.status = False
        else:
            print("Microwave already turned off")

    def run(self, seconds: int) -> None:
        """Function for running microwave"""
        if self.status:
            print(f"Running {self.brand} for {seconds} seconds")
        else:
            print("Microwave is turned off")

    def __add__(self, other) -> str:  # Dunder method
        return f"{self.brand} + {other.brand}"

    def __str__(self) -> str:
        return f"{self.brand} {self.power}"


smeg: Microwave = Microwave("Smeg", "C")
bosch: Microwave = Microwave("Bosch", "D")

print(smeg)
print(smeg.power)

smeg.turn_on()
smeg.run(30)
smeg.turn_off()

#
print(smeg + bosch)

print(smeg)
print(bosch)
