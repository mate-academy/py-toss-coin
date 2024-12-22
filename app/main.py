import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    coin_side = ["head", "tail"]

    for _ in range(10_000):
        heads = sum(random.choice(coin_side) == "head" for _ in range(10))
        if heads in result:
            result[heads] += 1
        else:
            result[heads] = 1

    percentages = {key: round((value / 10_000) * 100, 2)
                   for key, value
                   in result.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_values = sorted(data.keys())
    y_values = [data[key] for key in x_values]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values,
             y_values,
             marker="o",
             linestyle="-",
             color="blue",
             label="Distribution")

    plt.title("Gaussian Distribution of Heads in 10 Flips", fontsize=16)
    plt.xlabel("Number of Heads", fontsize=14)
    plt.ylabel("Percentage (%)", fontsize=14)
    plt.xticks(range(min(x_values), max(x_values) + 1))
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=12)

    plt.show()
