import random
import matplotlib.pyplot as plt


def flip_coin(num_flips: int=10, num_trials: int=10000) -> float: # noqa
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: list) -> list:
    x_coords = list(data.keys())
    y_coords = list(data.values())

    plt.bar(x_coords, y_coords, color="skyblue")
    plt.title("Distribution of Heads in Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(x_coords)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


results = flip_coin()
print(results)
draw_gaussian_distribution_graph(results)
