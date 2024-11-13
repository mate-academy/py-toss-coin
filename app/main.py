import random
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> dict:

    head_counts = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        head_counts[heads] += 1

    head_percentages = {k: (v / num_cases) * 100
                        for k, v in head_counts.items()}

    return head_percentages


def draw_gaussian_distribution_graph(head_percentages: dict) -> None:
    # Prepare data for plotting
    heads = list(head_percentages.keys())
    percentages = list(head_percentages.values())

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.bar(heads, percentages, color="blue", alpha=0.7, width=0.6)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(heads)  # Set x-ticks to be the heads counts
    plt.grid(axis="y")
    plt.show()
