import random


def flip_coin(flipping_count: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(flipping_count):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1
    for key in results:
        results[key] = round(results[key] / flipping_count * 100, 2)
    return results
