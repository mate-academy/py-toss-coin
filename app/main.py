import random
import matplotlib.pyplot as plt


def flip_coin() -> float:
    result = {key: 0 for key in range(0, 11)}
    for i in range(0, 10000):
        heads = 0
        for flip in range(0, 10):
            coin_flip = random.randint(0, 1)
            if coin_flip == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round((result[key] / 10000) * 100, 2)

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_axis = list(result.keys())
    y_axis = list(result.values())

    plt.bar(x_axis, y_axis, color="blue", alpha=0.7)

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of 10 Coin Flips")

    plt.show()
