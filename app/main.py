import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
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
    for _ in range(1000):
        number = [random.choice(["heads", "tails"])
                  for _ in range(10)].count("heads")
        result[number] += 1

    for i in range(len(result)):
        result[i] = round(result[i] / 1000 * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    resulting_dict = flip_coin()
    resulting_list = [item for item in resulting_dict.values()]
    plt.plot(resulting_list)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
