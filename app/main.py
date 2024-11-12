import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    outcomes = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        outcomes[heads_count] += 1

    percentages = {heads: (count / num_trials) * 100
                   for heads, count in outcomes.items()}

    return percentages


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
