import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["head", "other"]
    dict_head = {}
    for _ in range(10000):
        count_head = 0
        for _ in range(10):
            if random.choice(coin) == "head":
                count_head += 1
        if count_head in dict_head:
            dict_head[count_head] += 1
        else:
            dict_head[count_head] = 1

    for key, percent in dict_head.items():
        dict_head[key] = round(percent / 100, 3)
    return dict_head


def draw_gaussian_distribution_graph(dict_head: dict) -> None:
    x_point = []
    y_point = []
    for x_axis, y_axis in dict_head.items():
        x_point.append(x_axis)
        y_point.append(y_axis)

    plt.plot(x_point, y_point)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
