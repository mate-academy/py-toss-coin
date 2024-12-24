from random import randint

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")


def simulate_ten_flips() -> int:
    return sum(randint(0, 1) for _ in range(10))


def flip_coin(num_trials: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = simulate_ten_flips()
        results[heads_count] += 1

    for heads in results:
        results[heads] = round((results[heads] / num_trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_coords = list(data.keys())
    y_coords = list(data.values())

    plt.bar(x_coords, y_coords, color="blue", alpha=0.7, edgecolor="black")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("distribution_graph.png")


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)