import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    dict_num = {}
    res = []
    for _ in range(num_trials):
        results = sum([random.randint(0, 1) for _ in range(10)])
        res.append(results)
    count = Counter(res)
    for num in range(0, 11):
        dict_num.update({num: ((count[num] / num_trials) * 100)})

    return dict_num


def draw_gaussian_distribution_graph() -> None:
    value = flip_coin()
    xxx = value.keys()
    yyy = value.values()
    plt.plot(xxx, yyy)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
