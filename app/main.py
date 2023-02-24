from random import random


def flip_coin() -> dict:
    results = {}
    num_trials = 10000

    for i in range(num_trials):
        num_heads = 0
        for j in range(10):
            if random() < 0.5:
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for k in results:
        results[k] = round(results[k] / num_trials * 100, 2)

    return results
