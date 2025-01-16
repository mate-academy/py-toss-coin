import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = sorted(data.keys())
    values = [data[k] for k in keys]

    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color="blue", alpha=0.7)
    plt.title("Gaussian Distribution of Coin Flips "
              "(10 flips, 10000 simulations)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(range(0, 11))
    plt.show()
