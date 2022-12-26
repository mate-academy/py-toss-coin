import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    static_dict = {x: 0 for x in range(11)}
    for _ in range(10000):
        head = 0
        for item in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                head += 1
        static_dict[head] += 1
    for key, value in static_dict.items():
        static_dict[key] = round(value / 10000 * 100, 2)
    return static_dict


def draw_gaussian_distribution_graph(flips: dict) -> None:
    plt.plot(flips.keys(), flips.values())
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    flip_coin()
    draw_gaussian_distribution_graph(flip_coin())
