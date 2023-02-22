import numpy as np


def flip_coin() -> dict:
    results = {}
    flips = 10000
    for i in range(11):
        results[i] = 0
    for i in range(flips):
        heads = np.random.binomial(10, 0.5)
        results[heads] += 1
    for key in results:
        results[key] = round((results[key] / flips) * 100, 2)
    return results
