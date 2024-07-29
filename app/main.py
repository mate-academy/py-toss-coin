import random
from collections import Counter


def flip_coin(trials: int = 10000) -> dict[int, float]:
    results = []

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results.append(heads_count)

    counts = Counter(results)
    percentages = {
        key: (value / trials) * 100 for key, value in counts.items()
    }

    for number in range(11):
        if number not in percentages:
            percentages[number] = 0.0

    return percentages
