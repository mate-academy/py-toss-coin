import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        coins_list = [random.choice(("heads", "tails")) for _ in range(10)]
        heads_count = coins_list.count("heads")
        if heads_count in result:
            result[heads_count] += 1
        else:
            result[heads_count] = 1
    for key, value in result.items():
        result[key] = (value / 10000) * 100
    print(result)
    return result

# def draw_gaussian_distribution_graph() -> None:
#     result = flip_coin()
#     sorted_result = dict(sorted(result.items()))
#     print(sorted_result)
#     xpoint = np.array([int(key) for key in sorted_result])
#     ypoint = np.array([value for value in sorted_result.values()])
#
#     plt.title("gaussian distribution")
#     plt.xlabel("heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.plot(xpoint, ypoint)
#     plt.show()
#
# draw_gaussian_distribution_graph()
