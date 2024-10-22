from random import randint


def flip_coin() -> dict[int: float]:
    flip_times = dict.fromkeys(range(0, 11), 0)

    for _ in range(10000):
        temp = 0
        for _ in range(10):
            if randint(0, 1):
                temp += 1
        flip_times[temp] += 1

    return {
        key: value / 100
        for key, value in flip_times.items()
    }
