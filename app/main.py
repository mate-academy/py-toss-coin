from random import choice

from matplotlib import pyplot as plt


def draw_gaussian_distribution_graph(sorted_heads: list) -> None:
    x_axis = [x[0] for x in sorted_heads]
    y_axis = [y[1] for y in sorted_heads]

    plt.plot(x_axis, y_axis, color="blue")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.xticks(x_axis)
    plt.yticks([num for num in range(0, 101, 10)])
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.savefig("gaussian_distribution.png")


def flip_coin() -> dict:
    heads = {}
    coin = ["head", "tail"]
    for _ in range(10000):
        result = [choice(coin) for _ in range(10)].count("head")
        if heads.get(result):
            heads[result] += 1
        else:
            heads[result] = 1
    heads = {key: val / 100 for key, val in heads.items()}
    sorted_heads = sorted(heads.items(), key=lambda x: x[0])
    draw_gaussian_distribution_graph(sorted_heads)

    return heads
