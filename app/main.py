import random
from collections import Counter


def flip_coin():
    head_appearing_frequency = Counter(
        [random.choice(["head", "tail"]) for _ in range(10)].count("head")
        for _ in range(10000)
    )

    head_appearing_percentage = {
        key: round(value / 100)
        for key, value in sorted(head_appearing_frequency.items())
    }

    return head_appearing_percentage
