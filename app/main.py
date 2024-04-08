import random


def flip_coin() -> dict:
    flip_stats = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        num_heads = sum(random.random() < 0.5 for _ in range(10))
        flip_stats[num_heads] += 1

    percentages = {
        num_heads:
            (count / total_cases) * 100 for num_heads,
        count in flip_stats.items()
    }

    return percentages
