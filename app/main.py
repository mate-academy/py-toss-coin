import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    # Convert counts to percent
    percent = {
        key: (value / num_trials) * 100 for key,
        value in results.items()
    }

    return percent


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values, color="blue", alpha=0.7)
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.xticks(keys)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    percentages = flip_coin()

    print("Percentage distribution of heads in 10 coin flips:")
    for key, value in percentages.items():
        print(f"{key}: {value: .2f}%")

    draw_gaussian_distribution_graph(percentages)
