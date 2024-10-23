import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    results = []
    for _ in range(cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results.append(heads_count)

    counts = Counter(results)
    percentages = {
        key: (round((value / cases * 100), 2))
        for key, value in counts.items()
    }
    return percentages
