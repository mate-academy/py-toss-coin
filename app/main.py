import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin():
    trials = 10000
    n = 10
    heads = []
    for _ in range(trials):
        tosses = [random.random() for _ in range(n)]
        heads.append(len([i for i in tosses if i >= 0.5]))
    result = dict(Counter(heads))

    for key in result:
        result[key] = int((result[key] / trials) * 100)

    sort_dict = dict(sorted(result.items(), key=lambda x: x[0]))
    return sort_dict


def draw_gaussian_distribution_graph():
    graph = flip_coin()
    fig, ax = plt.subplots()
    plt.xlim([0, 10])
    plt.ylim([0, 100])
    plt.xticks(list(range(11)))
    plt.yticks(list(range(0, 101, 10)))
    plt.bar(*zip(*graph.items()))
    ax.set_title("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
