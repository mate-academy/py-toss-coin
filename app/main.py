import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    result_dict = {x: 0 for x in range(0, 11)}
    for _ in range(10000):
        count = 0
        for toss in range(10):
            toss = random.randint(0, 1)
            if toss == 1:
                count += 1
        result_dict[count] += 1

    for key in result_dict:
        result_dict[key] = round(
            0.01 * result_dict[key], 2
        )

    return result_dict


def draw_gaussian_distribution_graph() -> plt:
    result_dict = flip_coin()
    x_coords = list(result_dict.keys())
    y_coords = list(result_dict.values())
    plt.plot(x_coords, y_coords)
    plt.yticks(range(0, 110, 10))
    plt.xticks(range(0, 11, 1))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
