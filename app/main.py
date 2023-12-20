import matplotlib.pyplot as plt
import random


def flip_coin() -> dict[int: float]:

    result_dict = {num: 0 for num in range(11)}

    for _ in range(10000):
        result = sum(random.randint(1, 2) == 2 for _ in range(10))
        result_dict[result] += 1

    for key in result_dict:
        result_dict[key] = result_dict[key] * 100 / 10000

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.title("Gaussian distribution")

    plt.show()
