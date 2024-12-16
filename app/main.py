import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {
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
    drop_options = ["heads", "tails"]

    for case_number in range(0, 10000):
        count = 0

        for flip_number in range(0, 10):
            drop_result = random.choice(drop_options)
            if drop_result == "heads":
                count += 1

        result_dict[count] += 0.01

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    result_dict = flip_coin()

    x_points = []
    y_points = []
    for x_point, y_point in result_dict.items():
        x_points.append(x_point)
        y_points.append(y_point)

    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
