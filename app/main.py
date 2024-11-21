import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    """
    Simulates 10 coin flips in 10000 trials and calculates the percentage
    of each possible heads count (0 to 10).

    Returns:
        Dict[int, float]: A dictionary where keys are numbers of heads
        (0-10) and values are their percentage occurrences.
    """
    trials: int = 10000
    results: Dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count: int = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Convert counts to percentages
    percentages: Dict[int, float] = {
        k: (v / trials) * 100 for k, v in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    """
    Draws a Gaussian distribution graph using the data provided.

    Args:
        data (Dict[int, float]): A dictionary where keys are numbers of heads
        and values are their percentage occurrences.
    """
    heads = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads, percentages, color="blue", marker="o", linestyle="-")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Run simulation
    distribution = flip_coin()
    print(distribution)

    # Draw Gaussian distribution graph
    draw_gaussian_distribution_graph(distribution)
