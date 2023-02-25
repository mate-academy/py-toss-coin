import random


def flip_coin() -> dict:
    result_dict = {}
    result_ls = []

    for i in range(1000):
        result_flip = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 0:
                result_flip += 1
        result_ls.append(result_flip)

    result_ls = sorted(result_ls)
    for result in result_ls:
        if result not in result_dict:
            result_dict[result] = round(result_ls.count(result)
                                        / 1000 * 100, 2)
    return result_dict
