import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 0:
                counter += 1

        result[counter] += 1

    result = {key: round(((value * 100) / 10000), 2)
              for key, value in result.items()}
    return result


def draw_gaussian_distribution_graph() -> None:
    graph = flip_coin()
    graph_coords = list(sorted(graph.items()))
    y_coords = [i[1] for i in graph_coords]
    plt.plot(y_coords)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
