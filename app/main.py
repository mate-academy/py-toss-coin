import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(10 + 1)}

    total_flip = 10000

    for _ in range(total_flip):
        head_flip = sum(1 for _ in range(10) if random.random() < 0.5)
        result[head_flip] += 1

    for key in result:
        result[key] = round((result[key] / total_flip) * 100, 2)

    return result
