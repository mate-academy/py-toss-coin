from random import choice
import matplotlib.pyplot as plt


def flip_coin():
    data = dict.fromkeys(([x for x in range(0, 11)]), 0)
    flip_choice = ["heads", "tails"]
    result = []
    for case_ in range(10000):
        count_ = 0
        for i in range(10):
            if choice(flip_choice) == "heads":
                count_ += 1
        result.append(count_)
    for i in range(0, 11):
        value_ = (result.count(i) / 10000) * 100
        data[i] = value_
    return data


def draw_gaussian_distribution_graph():
    data = flip_coin()
    plt.axis([0, 10, 0, 100])
    plt.title("Gussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    x_coord = data.keys()
    y_coord = data.values()
    plt.plot(x_coord, y_coord)


if __name__ == "main":
    flip_coin()
