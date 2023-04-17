import random


def flip_coin() -> dict:
    times_dict = {a: 0 for a in range(0, 11)}
    for i in range(10000):
        lap = sum([random.randint(0, 1) for j in range(10)])
        times_dict.update({lap: times_dict[lap] + 1})
    result = {
        key: round(value / 10000 * 100, 2)
        for key, value in times_dict.items()
    }
    return result
