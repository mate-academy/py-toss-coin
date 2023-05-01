import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_flips = []
    for _ in range(15000):
        flips_list = []
        for flip in range(10):
            flips_list.append(random.choice(["head", "tail"]))
        count_flips.append(flips_list.count("head"))

    return {
        number: (count_flips.count(number) * 100) / 15000
        for number in range(11)
    }


def draw_gaussian_distribution_graph() -> None:
    func = flip_coin()
    plt.plot(func.keys(), func.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
