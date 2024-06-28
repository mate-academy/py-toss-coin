import random
from collections import defaultdict


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> dict:
    outcomes = defaultdict(int)

    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        outcomes[heads_count] += 1

    # Конвертуємо кількість випадків у відсотки
    percentages = {k: (v / num_cases) * 100 for k, v in outcomes.items()}

    return percentages
