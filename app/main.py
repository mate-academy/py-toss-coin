from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(total_cases):
        heads_count = 0

        for _ in range(10):
            if randint(0, 1) == 1:
                heads_count += 1

        results[heads_count] += 1

    percentages = {key: (value / total_cases) * 100
                   for key, value in results.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    resault_dict = flip_coin()
    plt.plot(*zip(*sorted(resault_dict.items())))
    plt.show()
