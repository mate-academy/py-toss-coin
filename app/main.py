import numpy as nmp

from random import choice
from matplotlib import pyplot as plt


def count_of_heads_from_10() -> int:
    return sum([choice([1, 0]) for _ in range(10)])


def flip_coin() -> dict:
    flip_count: int = 10000
    result_dict: dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(flip_count):
        count_from_10_value: int = count_of_heads_from_10()
        count_from_dict: int = result_dict.get(count_from_10_value)
        result_dict[count_from_10_value] = count_from_dict + 1
    return {
        key: value / flip_count * 100 for key, value in result_dict.items()
    }


def draw_gaussian_distribution_graph(graph: dict) -> None:
    xpoints = nmp.array([key for key in graph.keys()])
    ypoints = nmp.array([value for value in graph.values()])
    plt.plot(xpoints, ypoints)
    plt.xlabel("Count_of_coin_heads_from_10")
    plt.ylabel("Probability")
    plt.show()
