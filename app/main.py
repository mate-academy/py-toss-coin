# write your code here
import random
# from matplotlib import pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    total_dict = {}
    super_total_dict = {}
    for i in range(10000):
        heads_count = 0
        for _ in range(10):
            heads_count += random.randint(0, 1)
        total_dict[heads_count] = (total_dict.get(heads_count, 0) + 1)
    for key, value in total_dict.items():
        super_total_dict[key] = round(value / 100, 3)
    print(super_total_dict)
    super_total_dict = dict(sorted(super_total_dict.items()))
    return super_total_dict


# def draw_gaussian_distribution_graph() -> None:
#     coord_dict = flip_coin()
#
#     x = np.array(coord_dict.keys())
#     y = np.array(coord_dict.values())
#     plt.plot(x, y)
#     plt.show()
