import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            side_of_coin = random.randint(0, 1)
            if side_of_coin == 1:
                heads_count += 1
        results[heads_count] += 1

    for key, value in results.items():
        results[key] = round((value / 10000) * 100, 2)
    print(results)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_values = np.array(list(results.keys()))
    y_values = np.array(list(results.values()))

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.grid(axis="y", alpha=0.7, linestyle="--")

    plt.figure(figsize=(10, 6))

    # Add plot line for x and y values
    plt.plot(x_values, y_values, color="skyblue")

    # Set x and y axis limits
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin())
