import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_flips = 10000
    heads = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in range(total_flips):
        heads_of_round = 0
        for repeat_of_round in range(10):
            if random.randint(0, 1):
                heads_of_round += 1
        heads[heads_of_round] += 1
    for i in heads:
        heads[i] *= 100
        heads[i] /= total_flips
    return heads


def draw_gaussian_distribution_graph() -> None:
    probabilities = flip_coin()
    plt.plot(probabilities.keys(), probabilities.values())
    plt.xlim((0, 10))
    plt.ylim((0, 100))
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian distribution")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()


draw_gaussian_distribution_graph()
