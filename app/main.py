import random


def flip_coin() -> dict:
    result_dict = {
        i: 0 for i in range(11)
    }
    for _ in range(10000):
        flips = (
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1)
        )
        occurrences = flips.count(1)
        result_dict[occurrences] += 1
    for key in result_dict:
        result_dict[key] = round((result_dict[key] / 10000) * 100, 2)
    return result_dict:
