import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_results = []
    trials = 15000
    count = 0
    while count != trials:
        result_10_times = []
        for i in range(10):
            res = random.choice(["heads", "tails"])
            result_10_times.append(res)
        heads_count = result_10_times.count("heads")
        total_results.append(heads_count)
        count += 1
    counts = Counter(total_results)
    percentages = {k: (v / trials) * 100 for k, v in counts.items()}
    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(data: dict) -> None:
    outcomes = list(data.keys())
    percentages = list(data.values())

    # Plot the line graph with specified style
    plt.figure(figsize=(8, 6))
    plt.plot(outcomes, percentages, color="blue",
             marker="o", linestyle="-", linewidth=1)

    # Set title and axis labels with adjusted font sizes
    plt.title("Gaussian distribution", fontsize=14)
    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Drop percentage %", fontsize=12)

    # Set y-axis limit to match the scale in the example
    plt.ylim(0, 100)

    # Customize tick parameters for a similar look
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Display grid lines for the y-axis only
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Show the plot
    plt.show()


flip_data = flip_coin()
draw_gaussian_distribution_graph(flip_data)
