import random
import matplotlib.pyplot as plt


def flip_coin(
        num_trials: int = 10000,
        num_flips: int = 10
) -> dict:
    results = {}
    for _ in range(num_trials):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1
    for key in results:
        results[key] = round(results[key] / num_trials * 100, 2)
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    keys = sorted(results.keys())
    values = [results[key] for key in keys]
    mean = (
        sum(keys[i] * values[i]
            for i in range(len(keys)))
        / sum(values)
    )
    variance = (
        sum(values[i] * (keys[i] - mean) ** 2
            for i in range(len(keys))) / sum(values)
    )
    std_dev = variance ** 0.5
    plt.plot(keys, values)
    plt.xlabel("Number of heads dropped")
    plt.ylabel("Percentage")
    plt.title("Gaussian distribution of coin flips")
    plt.text(
        0.05, 0.95, f"Mean: {mean:.2f}\nStd. Deviation:"
        f" {std_dev:.2f}", transform=plt.gca().transAxes,
        ha="left", va="top"
    )
    plt.show()
