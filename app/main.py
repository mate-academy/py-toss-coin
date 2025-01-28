import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for side in range(10000):
        result = sum(random.choice([1, 0]) for _ in range(10))
        result_dict[result] += 1
    for key in result_dict:
        result_dict[key] = round((result_dict[key] / 10000) * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_array = np.array(list(result.keys()))
    y_array = np.array(list(result.values()))
    plt.figure(figsize=(10, 5))
    plt.plot(x_array, y_array)
    plt.ylim([0, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph()
