import random
import matplotlib.pyplot as plt


def flip_once() -> int:
    heads_count = 0
    for _ in range(10):
        if random.choice([0, 1]) == 1:
            heads_count += 1
    return heads_count


def flip_experiment(trials: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = flip_once()
        results[heads_count] += 1
    percentages = {k: (v / trials) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
        heads_counts = list(data.keys())
        drop_percentages = list(data.values())
        plt.figure(figsize=(8, 6))
        plt.plot(
            heads_counts, drop_percentages,
            color="blue", marker="o", markersize=0, linestyle="-"
        )
        plt.title("Gaussian Distribution", fontsize=16)
        plt.xlabel("Heads Count", fontsize=12)
        plt.ylabel("Drop Percentage (%)", fontsize=12)
        plt.xlim(0, 10)
        plt.ylim(0, 100)
        plt.yticks(range(0, 101, 10))
        plt.xticks(range(0, 11))
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.show()

data = flip_experiment()
draw_gaussian_distribution_graph(data)