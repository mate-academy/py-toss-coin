import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_trials = 10000
    results = {i: 0 for i in range(11)}

    for count in range(num_trials):
        heads_count = sum(1 for count in range(10) if random.random() > 0.5)
        results[heads_count] += 1
    percentages = {
        heads: (count / num_trials) * 100 for heads, count in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    heads = list(data.keys())
    percentages = list(data.values())
    label_font = {"family": "serif", "fontsize": 12}
    title_font = {"family": "serif", "fontsize": 16, "fontweight": "bold"}
    plt.plot(heads, percentages, color="midnightblue")
    plt.xlabel("Heads count", fontdict=label_font)
    plt.ylabel("Drop percentage %", fontdict=label_font)
    plt.title("Gaussian distribution", fontdict=title_font)
    plt.ylim(0, 100)
    plt.show()
