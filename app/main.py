import random
# import numpy as np
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        dict_result[heads_count] += 1
    persentage = {
        key: value / 10000 * 100
        for key, value in dict_result.items()
    }
    return persentage
    # xpoints = np.array(list(persentage.keys()))
    # ypoints = np.array(list(persentage.values()))
    # plt.plot(xpoints, ypoints)
    # plt.show()
