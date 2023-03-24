from random import choice
import numpy as np
import matplotlib.pyplot as plt


def run_case() -> int:
    return sum([choice([0, 1]) for i in range(10)])


def flip_coin() -> dict:
    all_cases = []

    for i in range(10000):
        all_cases.append(run_case())

    result = {
        i: round((all_cases.count(i) / 10000) * 100, 2) for i in range(11)
    }
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    number_of_heads = np.array(list(result.keys()))
    percentage = np.array(list(result.values()))
    plt.title("Gaussian distribution graph")
    plt.xlabel("Number of heads dropped")
    plt.ylabel("Head drop percentage")
    plt.plot(number_of_heads, percentage)
    plt.show()
