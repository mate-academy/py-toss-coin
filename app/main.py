import random
import matplotlib.pyplot as plt


def flip_coin(simulations: int = 10000, n_flip: int = 10) -> dict:
    results = {i: 0 for i in range(n_flip + 1)}
    for _ in range(simulations):
        heads_count = sum(random.choice([0, 1]) for _ in range(n_flip))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / simulations) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_points = list(results.keys())
    y_points = list(results.values())
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")
    plt.show()
