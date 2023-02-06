import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_coin_head_values = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    cycles_number = 100

    for _ in range(cycles_number):
        random.seed(random.randint(0, 1000))
        count_head = 0
        for _ in range(10):
            flip_result = random.randint(0, 1)
            if flip_result == 1:
                count_head += 1

        flip_coin_head_values[count_head] += 1

    for key, values in flip_coin_head_values.items():
        flip_coin_head_values[key] = round(values / cycles_number, 2)

    return flip_coin_head_values


def draw_gaussian_distribution_graph(distribution_results: dict) -> None:
    point_x = np.array(list(distribution_results.keys()))
    point_y = np.array(list(distribution_results.values()))
    plt.plot(point_x, point_y)
    plt.xlabel("Number of occurrences of the obverse of the coin in the cycle")
    plt.ylabel("Number of repetitions of the loop value")
    plt.show()
