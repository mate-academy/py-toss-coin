from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for i in range(11):
        result[i] = 0
    cases = 10000
    for _ in range(cases):

        count = 0
        for _ in range(10):
            flip = choice([0, 1])
            if flip == 1:
                count += 1
        result[count] += 1

    return {index: (value * 100 / cases) for index, value in result.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    xpoints = []
    ypoints = []
    print(data)
    for index, persent in data.items():
        xpoints.append(index)
        ypoints.append(persent)
    plt.plot(xpoints, ypoints)
    plt.show()
