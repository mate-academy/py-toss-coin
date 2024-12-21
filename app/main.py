import random
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int: float]:
    heads_all_counts = []
    for _ in range(10000):
        heads_count = 0
        random.seed(random.randint(1,9999999))
        for _ in range(10):
            if random.choice(['heads', 'tails']) == 'heads':
                heads_count += 1
        heads_all_counts.append(heads_count)
    return {k: heads_all_counts.count(k) / len(heads_all_counts) for k in range(11)}

def draw_gaussian_distribution_graph():
    coins = flip_coin()
    xpoints = np.array(list(coins.keys()))
    ypoints = np.array([round(x * 100, 2) for x in list(coins.values())])


    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.title('Gaussian distribution')
    plt.ylim([0,100])
    plt.xlim([0,10])

    plt.plot(xpoints, ypoints)
    plt.xticks(range(11))
    plt.yticks(range(0,101,10))
    plt.show()


if __name__ == '__main__':
    cache = set()

    for _ in range(20):
        coins = flip_coin()

        cache.add(tuple(result for result in coins.values()))
    print(cache)
    draw_gaussian_distribution_graph()