import random
import matplotlib.pyplot as plt


def flip_coin(count: int = 10000):
    result_dict = {i: 0 for i in range(0, 11)}
    flip = ["heads", "tails"]
    result = []

    for _ in range(count):
        sum_heads = 0
        for x in range(0, 10):
            if random.choice(flip) == "heads":
                sum_heads += 1
        result.append(sum_heads)

    for val in range(0, 11):
        value = (result.count(val) / 10000) * 100
        result_dict[val] = value

    return result_dict


def draw_gaussian_distribution_graph():
    fig, ax = plt.subplots()
    data = flip_coin()

    # Adding axis labels and title
    ax.settitle("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")

    # Building graph
    x = data.keys()
    y = data.values()
    ax.plot(x, y)
    ax.grid()
