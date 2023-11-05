import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips: int = 10, ) -> dict:
    toss_counter = defaultdict(float)

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        toss_counter[heads] += 1

    for toss in toss_counter:
        toss_counter[toss] = round((toss_counter[toss] / trials) * 100, 2)

    return dict(toss_counter)


def draw_gaussian_distribution_graph(data: dict) -> None:
    sorted_data = dict(sorted(data.items()))

    x_ = list(sorted_data.keys())
    y_ = list(sorted_data.values())
    print("X=", x_)
    print("y=", y_)

    plt.ylabel("Drop  percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")
    plt.plot(x_, y_)

    plt.show()
