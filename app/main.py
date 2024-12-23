import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        flip_res = [random.choice([0, 1]) for _ in range(10)]
        head = sum(flip_res)
        result[head] += 1

    for key in result:
        result[key] = round((result[key] / 10000) * 100, 2)

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_ = list(result.keys())
    y_ = list(result.values())

    plt.plot(x_, y_)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.show()
