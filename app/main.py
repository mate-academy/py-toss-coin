import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    result = {key: value / num_cases * 100 for key, value in results.items()}
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())
    plt.plot(keys, values)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
