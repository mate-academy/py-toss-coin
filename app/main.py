import random


def flip_coin() -> dict:
    results = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
        5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    num_cases = 10000

    for _ in range(num_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    for num_heads in results:
        results[num_heads] = round(results[num_heads] / num_cases * 100, 2)

    return results
