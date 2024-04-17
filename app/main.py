import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    print(results)
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1
    percentages = {key: (value / 10000 * 100)
                   for key, value in results.items()}
    return percentages
