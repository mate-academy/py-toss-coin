import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    cases = 10000
    flips = 10
    total_flips = 0
    for i in range(cases):
        heads_count = 0
        for _ in range(flips):
            flip = random.randint(0, 1)
            if flip == 0:
                heads_count += 1
        total_flips += 1
        result[heads_count] += 1

    for key in result:
        result[key] = round((result[key] / total_flips) * 100, 2)

    return result


def draw_gaussian_distribution_graph(percentage_data: dict) -> None:
    percentages = [percent for percent in percentage_data.values()]

    ids = [x for x in range(len(percentages))]

    plt.plot(ids, percentages)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.show()
