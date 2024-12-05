import random
from matplotlib import pyplot as plt


def flip_coin(num_trials: int = 10000, flips_per_trial: int = 10) -> dict:
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results


def draw_gaussian_distribution_graph(result: dict) -> None:

    x_axis = list(result.keys())
    y_axis = list(result.values())

    plt.figure(figsize=(8, 5))
    plt.plot(x_axis, y_axis, marker="o", linestyle="-", color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
