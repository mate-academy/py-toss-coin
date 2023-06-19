import random


def flip_coin() -> dict:
    results = {}
    total_cases = 10000

    for i in range(total_cases):
        heads_count = 0

        for i in range(10):
            if random.random() < 0.5:
                heads_count += 1

        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1

    for heads, count in results.items():
        results[heads] = (count / total_cases) * 100

    return results
