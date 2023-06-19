import random


def flip_coin() -> dict:
    results = {}

    num_cases = 10000
    num_flips = 10

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.choice(["head", "tail"]) == "head":
                num_heads += 1

        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for num_heads in results:
        results[num_heads] = (results[num_heads] / num_cases) * 100

    return results
