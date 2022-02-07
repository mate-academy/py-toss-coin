import random
import matplotlib.pyplot as plt


def flip_coin():
    heads_odds = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                  6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
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
    drop = []
    heads = []
    for key, value in odds_dict.items():
        drop.append(value)
        heads.append(key)
    plt.plot(heads, drop)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.savefig("filename.png")
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
