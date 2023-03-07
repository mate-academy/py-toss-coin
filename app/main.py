import random


def flip_coin() -> dict:
    result_dict = {}

    for _ in range(10000):
        coins_flips_list = [random.choice((0, 1)) for _ in range(10)]
        heads_count = coins_flips_list.count(0)

        if heads_count in result_dict:
            result_dict[heads_count] += 1

        else:
            result_dict[heads_count] = 1

    for key, value in result_dict.items():
        result_dict[key] = (value / 10000) * 100

    return result_dict
