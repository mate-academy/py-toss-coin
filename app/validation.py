def validate_positive_integer(value: str) -> int | None:
    """
    Validates and converts a single input string into a positive integer
    """
    while True:
        try:
            value_int = int(value)
            if value_int < 0:
                raise ValueError("Flips cannot be negative.")
            return value_int
        except ValueError:
            print("Error flips: Enter an integer!")
            value = input("Enter number of flips again: ")


def input_data() -> tuple[int, int]:
    """
    Requests and validates two integers from the user
    """
    flips = validate_positive_integer(input("Enter the number of flips: "))
    amount = validate_positive_integer(input("Enter the amount of coins: "))
    return flips, amount
