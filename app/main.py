from random import randint
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, float]:
    cases: dict[int, int] = dict.fromkeys(range(0, 11), 0)
    for _ in range(1, 10001):
        num_heads = sum(randint(0, 1) for _ in range(10))
        cases[num_heads] += 1
    return {
        num: round(num_cases / 100, 2)
        for num, num_cases in cases.items()
    }


def draw_gaussian_distribution_graph(cases: dict[int, float]) -> None:
    xpoints = np.array([*cases.keys()])
    ypoints = np.array([*cases.values()])

    plt.title("Guassian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.plot(xpoints, ypoints)

    plt.show()
