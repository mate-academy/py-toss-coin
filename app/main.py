import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

CASES = 10000


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
              10: 0}
    head_tail = ["head", "tail"]
    for case in range(CASES):
        temporary_res = 0
        for _ in range(10):
            if head_tail[random.randint(0, 1)] == "head":
                temporary_res += 1

        if temporary_res in result:
            result[temporary_res] += 1

    return {key: (value / 100) for key, value in result.items()}


def draw_gaussian_distribution_graph() -> None:
    data_dict = flip_coin()
    list_value = list(data_dict.values())
    y_point = np.array(list_value)

    mpl.use("TkAgg")
    plt.plot(y_point)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph()
