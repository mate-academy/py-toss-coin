import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    trials = 10000

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100

    return results


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_points = list(distribution.keys())
    y_points = list(distribution.values())

    plt.plot(x_points, y_points, "b-")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.gca().yaxis.set_ticks(range(5, 101, 5), minor=True)
    plt.show()


draw_gaussian_distribution_graph()
