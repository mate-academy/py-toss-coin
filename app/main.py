import matplotlib.pyplot as plt

from random import randint


def flip_coin() -> dict:
    head_chances = {}
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            if randint(1, 2) == 1:
                count_heads += 1
        head_chances[count_heads] = head_chances.get(count_heads, 0) + 1
    return {
        key: (head_chances[key] * 100) / 10000
        for key in sorted(head_chances)
    }


def draw_gaussian_distribution_graph() -> None:
    chances = flip_coin()
    xpoints = list(chances.keys())
    ypoints = list(chances.values())

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
