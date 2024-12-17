import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        number = sum(random.choice([0, 1]) for _ in range(10))
        result_dict[number] += 1
    percentages = {
        key: round((value / 100), 2) for key, value in result_dict.items()
    }
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    axis_x = list(data.keys())
    axis_y = list(data.values())

    plt.plot(axis_x, axis_y)

    plt.title("Gaussian Distribution")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")

    plt.show()
