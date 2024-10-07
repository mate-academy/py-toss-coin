from numpy import random


def flip_coin(num_experiments: int = 10000) -> dict:
    statistics = {i: 0 for i in range(11)}
    for _ in range(num_experiments):
        result = random.binomial(n=10, p=0.5)
        statistics[result] += 1

    percentages = {key: (value / num_experiments) * 100
                   for key, value in statistics.items()}

    return percentages


print(flip_coin())
