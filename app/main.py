import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                heads_count += 1
        result[heads_count] += 1
    for key, value in result.items():
        result[key] = (value / 10000) * 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_points = (list(result.keys()))
    y_points = (list(result.values()))
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
