import random
import matplotlib.pyplot as plt


def flip_coin():
    times = 10
    heads_odds = {key: 0 for key in range(times + 1)}
    for i in range(10000):
        heads_count = 0
        for j in range(10):
            variant = random.randint(1, 2)
            if variant == 1:
                heads_count += 1
        heads_odds[heads_count] += 1
    for keys in heads_odds:
        heads_odds[keys] = int((heads_odds[keys] / 10000) * 100)
    return heads_odds


def draw_gaussian_distribution_graph():
    odds_dict = flip_coin()
    plt.plot(odds_dict.keys(), odds_dict.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.savefig("filename.png")
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
