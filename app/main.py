import random


def flip_coin(
        num_cases: int = 10000,
        num_flips: int = 10
) -> dict:
    results = {}

    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] = results.get(heads_count, 0) + 1

    percentages = {
        key: value / num_cases * 100
        for key, value
        in results.items()
    }
    return percentages
