import random
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:  # Assuming a fair coin
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for key in results:
        results[key] = (results[key] / num_cases) * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    sorted_results = dict(sorted(results.items()))
    plt.plot(
        sorted_results.keys(),
        sorted_results.values(),
        marker="o",
        color="blue",
    )
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.xticks(range(11))
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    draw_gaussian_distribution_graph(results)
