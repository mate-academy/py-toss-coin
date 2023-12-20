import random


def flip_coin() -> dict[int: float]:

    flips = 10000
    tosses = 10

    results = {}

    for _ in range(flips):
        heads = sum(random.choice([0, 1]) for _ in range(tosses))
        results[heads] = results.get(heads, 0) + 1

    result = {key: (value / flips) * 100 for key, value in results.items()}

    return result
