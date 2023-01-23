import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = {}
    for number in range(11):
        match_number = 0
        for _ in range(10000):
            number_flip = 0
            for _ in range(10):
                if random.randint(1, 2) == 1:
                    number_flip += 1
            if number_flip == number:
                match_number += 1
        coin.update({number: (match_number / 10000) * 100})
    return coin


def draw_gaussian_distribution_graph() -> None:
    plt.plot([i for i in flip_coin().values()])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
