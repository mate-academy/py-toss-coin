import random


def flip_coin() -> dict:
    results = {}
    num_cases = 10000

    for num_heads in range(11):
        results[num_heads] = 0

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1

    for num_heads in range(11):
        results[num_heads] = results[num_heads] / num_cases * 100

    return results
