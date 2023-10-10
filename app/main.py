import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {}
    for i in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))

        if heads in flip_dict:
            flip_dict[heads] += 1
        else:
            flip_dict[heads] = 1

    output_dict = {}
    for heads, count in flip_dict.items():
        probability = (count / 10000) * 100
        output_dict[heads] = round(probability, 2)
    return dict(sorted(output_dict.items()))


def draw_gaussian_distribution_graph(prob_dict: dict) -> None:
    plt.title("Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")

    y_points = np.array([value for value in prob_dict.values()])
    plt.plot(y_points)
    plt.show()
