import random
from collections import Counter


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10

    num_heads_list = [
        sum(random.choice([0, 1])
            for _ in range(num_flips))
        for _ in range(num_cases)
    ]
    results = Counter(num_heads_list)

    percentages = {
        num_heads: count / num_cases * 100
        for num_heads, count in results.items()
    }
    return percentages
