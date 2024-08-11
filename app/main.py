import random

from matplotlib import pyplot as plt


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> dict:
    result_dict = {i: 0 for i in range(num_flips + 1)}

    for num in range(num_cases):
        coin_count = sum(random.randint(0, 1)
                         for num in range(num_flips))
        result_dict[coin_count] += 1

    for percent in result_dict:
        result_dict[percent] = round(result_dict[percent] / num_cases * 100, 2)

    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    dot_x = result_dict.keys()
    dot_y = result_dict.values()

    plt.plot(dot_x, dot_y)

    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    plt.show()
