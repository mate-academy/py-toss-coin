import random
import matplotlib.pyplot as plt
from collections import Counter
from typing import Dict


# Step 1: Define the flip_coin function
def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> Dict[int, float]:
    results = []

    # Run the simulation num_cases times
    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(num_flips))  # 1 represents heads
        results.append(heads_count)

    # Count occurrences of each possible number of heads (0 to 10)
    heads_counter = Counter(results)

    # Convert counts to percentages
    percentages = {
        heads: (count / num_cases) * 100 for heads,
        count in heads_counter.items()
    }

    return percentages


# Step 2: Define the function to draw the Gaussian distribution graph
def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    # Sort data by keys for a better-looking graph
    keys = sorted(data.keys())
    values = [data[k] for k in keys]

    plt.plot(keys, values, marker="o", linestyle="-")
    plt.title("Gaussian Distribution of Coin Flips (10 flips per case)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.show()


# Run the simulation and plot results
flip_results = flip_coin()
print(flip_results)
draw_gaussian_distribution_graph(flip_results)
