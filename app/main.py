from decimal import Decimal, getcontext
import random


def flip_coin(num_flips: int = 10000, num_coin_tosses: int = 10) -> dict:
    getcontext().prec = 28  # Set precision for Decimal calculations
    results = {i: Decimal("0") for i in range(num_coin_tosses + 1)}

    for _ in range(num_flips):
        # Simulate a coin toss 'num_coin_tosses' times
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coin_tosses))
        results[num_heads] += 1

    # Calculate percentages and convert Decimal to float
    percentages = {key: float(value / num_flips * Decimal("100"))
                   for key, value in results.items()}

    return percentages
