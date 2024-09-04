import random


def flip_coin() -> dict:
    coin_side = ["heads", "tails"]
    result_dict = {}
    for i in range(10000):
        list_of_flips = []
        for _ in range(10):
            list_of_flips.append(random.choice(coin_side))
        for key in range(11):
            if list_of_flips.count("heads") == key:
                if key in result_dict.keys():
                    result_dict[key] += 0.01
                    result_dict[key] = round(result_dict[key], 2)
                else:
                    result_dict[key] = 0.01
    result_dict_sorted = dict(sorted(result_dict.items()))
    return result_dict_sorted