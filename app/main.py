import matplotlib.pyplot as plt
import random


def flip_coin():
    expected = 10_000
    flip_number = 10
    expected_results = {i: 0 for i in range(flip_number + 1)}

    for _ in range(expected):
        results = {1: 0, 0: 0}
        for _ in range(flip_number):
            results[random.randint(0, 1)] += 1
        expected_results[results[1]] += 1

    for i in expected_results:
        expected_results[i] = int(
            (expected_results[i] / expected_results) * 100
        )
    return expected_results


def diagram_of_results():
    data = flip_coin()
    plt.bar(*zip(*data.items()))
    plt.ylim([0, 100])
    plt.show()
