import random
import matplotlib.pyplot as plt


def flip_coin():
    dict_0_to_10 = {i: 0 for i in range(11)}
    for i in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                # count = how many times we hit tails in 10 flips
                count += 1
        # the dictionary adds to the key with index = count : 1
        dict_0_to_10[count] += 1
    result = {key: value / 100 for key, value in dict_0_to_10.items()}
    return result


def draw_gaussian_distribution_graph():
    flip_coin()
    fig, ax = plt.subplots()

    y = flip_coin().values()
    x = flip_coin().keys()
    ax.plot(x, y, color="blue", linestyle="-", marker="o")

    ax.set_title("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")

    return plt.show()
