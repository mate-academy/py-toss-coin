import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    coin = ["head", "tail"]
    for _ in range(10000):
        flip = 0
        random.seed()
        for _ in range(10):
            flip += 1 if random.choice(coin) == "head" else 0
        flip_dict[flip] += 0.01
    return flip_dict


def draw_gaussian_distribution_graph(flips: dict) -> None:
    plt.plot(flips.keys(), flips.values())
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
