import random
import matplotlib.pyplot as plt
from scipy.stats import norm


def flip_coin(attempts: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(attempts):
        head_count = sum(random.choice([0, 1]) for _ in range(10))
        result[head_count] += 1

    head_count_percent = {
        heads: (count / attempts) * 100 for heads, count in result.items()
    }

    return head_count_percent


def draw_gaussian_distribution_graph(mean: float = 5,
                                     standard_deviation: float = 1) -> None:
    x_coord = [mean - 4 * standard_deviation + i
               * (8 * standard_deviation / 1000) for i in range(1000)]
    y_coord = [norm.pdf(x, mean, standard_deviation) for x in x_coord]

    plt.figure(figsize=(10, 6))
    plt.plot(x_coord, y_coord, color="blue", label="Gaussian Distribution")

    plt.title("Gaussian Distribution", fontsize=16)
    plt.xlabel("Heads count", fontsize=14)
    plt.ylabel("Drop percentage %", fontsize=14)
    plt.axvline(mean,
                color="black",
                linestyle="dashed",
                linewidth=1,
                label="Mean")

    plt.legend()
    plt.grid()
    plt.show()
