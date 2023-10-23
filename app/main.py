import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Convert counts to percentages
    total_cases = num_cases
    for key, value in results.items():
        results[key] = (value / total_cases) * 100

    return results
