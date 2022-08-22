import random
import matplotlib.pyplot as plt


def flip_coin():
    data = dict.fromkeys(([x for x in range(0, 11)]), 0)
    flip = ["heads", "tails"]
    result = []
    for amount in range(10000):
        sum_heads = 0
        for i in range(10):
            if random.choice(flip) == "heads":
                sum_heads += 1
        result.append(sum_heads)
    for i in range(0, 11):
        value = (result.count(i) / 10000) * 100
        data[i] = value
    return data


def draw_gaussian_distribution_graph():
    data = flip_coin()
    plt.axis([0, 10, 0, 40])
    plt.title("Gussian distribution")
    plt.xlabel("Heads")
    plt.ylabel("Drop %")
    x = data.keys()
    y = data.values()
    plt.plot(x, y)
    plt.show()


if __name__ == "main":
    flip_coin()
