import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        times = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                times += 1

        result_dict[times] += 1

    for key in result_dict:
        result_dict[key] = round(result_dict[key] / 10000, 3)

    return result_dict


print(flip_coin())
