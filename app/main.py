import random
import matplotlib.pyplot as plt


def flip_coin() -> float:
    results = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results


def draw_gaussian_distribution_graph(results: float) -> None:

    keys = list(results.keys())
    values = list(results.values())

    plt.plot(keys, values, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
