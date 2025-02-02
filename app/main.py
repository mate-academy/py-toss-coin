import random
import matplotlib.pyplot as plt

def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:
    flip_results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(random.randint(0, 1) for _ in range(flips))
        flip_results[heads_count] += 1

    for key in flip_results:
        flip_results[key] = round((flip_results[key] / trials) * 100, 2)

    draw_gaussian_distribution_graph(flip_results)
    return flip_results

def draw_gaussian_distribution_graph(flip_results: dict) -> None:
    plt.bar(
        flip_results.keys(),
        flip_results.values(),
        color="blue",
        alpha=0.7
    )
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

flip_results = flip_coin()
print(flip_results)

