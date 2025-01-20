import random
import math


def get_head_percent(size: int):
    flips = [bool(random.randint(0, 1)) for _ in range(size)]
    heads = sum(flips)
    return round(heads / size * 100, 2)


def flip_coin():
    statistic_dict = {}
    iterations = 10000
    size = 10
    for i in range(iterations):
        statistic_dict[i] = get_head_percent(size)
    return statistic_dict

