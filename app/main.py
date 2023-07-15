import random

import matplotlib


def flip_coin() -> dict:

    ten_flips_results = {
        "heads": 0,
        "tails": 0,
    }
    flip_cases = {
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
        10: 0,
    }
    flip_results = {}
    sides = list(ten_flips_results.keys())

    for _ in range(10000):
        for i in range(10):
            ten_flips_results[random.choice(sides)] += 1
        flip_cases[ten_flips_results["heads"]] += 1
        ten_flips_results["heads"] = 0
        ten_flips_results["tails"] = 0

    for key, value in flip_cases.items():
        flip_results[key] = round((value / 10000) * 100, 2)
    print(flip_results)

    return flip_results


def draw_gaussian_distribution_graph(flip_results: dict) -> None:
    x_values = list(flip_results.keys())
    y_values = list(flip_results.values())

    matplotlib.pyplot.plot(x_values, y_values, marker="o")
    matplotlib.pyplot.xlabel("Number of Heads")
    matplotlib.pyplot.ylabel("Percentage")
    matplotlib.pyplot.title("Gaussian Distribution of Heads Flipped")

    matplotlib.pyplot.show()
