import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {i: 0 for i in range(11)}
    for case in range(10000):
        count_of_heads = random.choices(["head", "tail"], k=10).count("head")
        flip_dict[count_of_heads] += 0.01
    return flip_dict


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()
    heads_count = flips.keys()
    drop_percentage = [value * 4 for value in flips.values()]
    plt.plot(heads_count, drop_percentage)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
