import random


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    result = {heads: 0 for heads in range(num_flips + 1)}

    for _ in range(num_cases):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1
        result[heads_count] += 1

    for key, value in result.items():
        result[key] = (value / num_cases) * 100

    return result
