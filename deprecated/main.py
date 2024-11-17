# This is testing deprecated in 3.13

from warnings import deprecated

def calculations(a: int, b: int) -> tuple[int, int]:
    return a + b, a * b

@deprecated("\nThis is deprecated\nUse calculations instead")
def old_calculations(a: int, b: int) -> tuple[int, int]:
    return a * b, a * b

def main() -> None:

    print(calculations(2, 3))
    print(old_calculations(2, 3))

    for x in locals():
        print(f'Local variable: {x}: {locals()[x]}')
    for x in globals():
        if '__' in x:
            continue
        print(f'Global variable: {x}: {globals()[x]}')


if __name__ == "__main__":
    main()

