import random
from matplotlib import pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}

    for _ in range(10000):
        head = 0
        for __ in range(10):
            if random.randint(0, 1) == 1:
                head += 1
        result[head] += 0.01

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    xpoints = np.array(list(data.keys()))
    ypoints = np.array(list(data.values()))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)
    plt.show()


# def draw_gaussian_distribution_graph() -> None:
#     flipped = flip_coin()
#     plt.plot(flipped.keys(), flipped.values())
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#     plt.show()

# def flip_coin() -> dict:
#     stats_dict = {}
#     for _ in range(10000):
#         heads = 0
#         tails = 0
#         for __ in range(10):
#             toss_value = random.choice(["heads", "tails"])
#             if toss_value == "heads":
#                 heads += 1
#             else:
#                 tails += 1
#         stats_dict[heads] = stats_dict.get(heads, 0) + 1
#     for key, value in stats_dict.items():
#         stats_dict[key] = round(value * 100 / 10000, 2)
#     return dict(sorted(stats_dict.items()))
