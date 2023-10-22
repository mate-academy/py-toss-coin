import random
from collections import defaultdict


def flip_coin() -> dict:
    res = defaultdict(lambda: 0)
    
    for _ in range(0, 10000):
        flips = sum([random.randint(0, 1) for _ in range(10)])
        res[flips] += (1 / 100)

    return res

