import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    total_list = []
    total_dict = {}
    range_ = 11000
    coin = ["head", "other_side"]
    for i in range(range_):
        head_count = 0
        for num in range(10):
            if random.choice(coin) == "head":
                head_count += 1
        total_list.append(head_count)

    for i in total_list:
        if i not in total_dict:
            total_dict[i] = total_list.count(i) / range_ * 100

    return total_dict


def draw_gaussian_distribution_graph(total_dict: dict) -> None:
    plt.bar(total_dict.keys(), total_dict.value())
    plt.xlabel = "Heads count"
    plt.ylabel = "Drop percentage %"
    plt.title = "Gaussian distribution"
    plt.show()
