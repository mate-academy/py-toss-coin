import random

import matplotlib.pyplot as plt


def flip_coin():
    coin = ["head", "tail"]
    head_in_ceases = []
    for _ in range(10_000):
        count_head_tail = {}
        for _ in range(10):
            choice = random.choice(coin)
            count_head_tail[choice] = count_head_tail.get(choice, 0) + 1
        head_in_ceases.append(count_head_tail.get("head", 0))
    for i in range(11):
        return {i: head_in_ceases.count(i) * 100 / 10000 for i in range(11)}


def draw_gaussian_distribution_graph():
    x = []
    y = []
    result_of_func = flip_coin()
    for key, value in result_of_func.items():
        x.append(key)
        y.append(value)
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.axis([0, 10, 0, 100])
    plt.plot(x, y, color='b', linewidth=2)
    plt.show()
