from random import randint

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    attempts = 10000
    result_in_attempt = {i: 0 for i in range(attempts)}
    for i in range(attempts):
        for _ in range(10):
            if randint(0, 1) == 1:
                result_in_attempt[i] += 1
    result = {i: 0.0 for i in range(11)}
    for i in range(11):
        value = sum(
            1 for value in result_in_attempt.values() if value == i
        ) * 100 / attempts
        result[i] = value
    return result


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_line = list(distribution)
    y_line = [value for value in distribution.values()]

    plt.ylim(0, 100)
    plt.plot(x_line, y_line, marker="o")
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)

    plt.show()
