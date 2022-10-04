import matplotlib.pyplot as plt

from random import choice


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}

    for flip in range(10000):
        count = 0
        flip = ("head", "tail")
        for i in range(10):
            if choice(flip) == "head":
                count += 1
        result[count] += 1
    print({key: value / 100 for key, value in result.items()})
    return {key: value / 100 for key, value in result.items()}


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.plot([value for value in points.values()], color="b")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
