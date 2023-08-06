import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {
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
        10: 0}

    choices = ("head", "tail")
    for action in range(100000):
        head_count = 0

        for flip in range(10):
            drop = random.choice(choices)
            if drop == "head":
                head_count += 1

        results[head_count] += 1

    for key, value in results.items():
        results[key] = round(value / 1000, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = (flip_coin())

    x_points = [key for key in results.keys()]
    y_points = [value for value in results.values()]

    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()
