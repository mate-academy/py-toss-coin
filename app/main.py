import random

import matplotlib.pyplot as mpl


def flip_coin() -> dict:
    temp_res = {}
    result = {}
    for case in range(10000):
        head = 0
        for flip in range(10):
            choice = random.choice(["head", "tail"])
            if choice == "head":
                head += 1
        temp_res[case] = head
    temp_res_values = temp_res.values()
    temp_res_values = list(temp_res_values)
    for i in range(0, 11):
        b = temp_res_values.count(i)
        result[i] = (b / 10000) * 100
    return result


def draw_gaussian_distribution_graph():
    x = list(flip_coin.keys())
    y = list(flip_coin.values())
    mpl.plot(x, y, 'o:r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
    mpl.xlabel("count of 'Head' in case")
    mpl.ylabel("percent of all cases")
    mpl.show()
