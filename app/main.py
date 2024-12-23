import random
import matplotlib.pyplot as plt


def flip_coin(
        num_experiments: int = 10000,
        flips_per_experiment: int = 10
) -> dict:
    results = {i: 0 for i in range(flips_per_experiment + 1)}

    for _ in range(num_experiments):
        heads_count = sum(
            random.choice([0, 1])
            for _ in range(flips_per_experiment)
        )
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_experiments) * 100, 2)

    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:

    xpoints = list(distribution.keys())
    ypoints: list[float] = list(distribution.values())

    plt.title("Gaussian distribution", loc="center")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(xpoints, ypoints)
    return plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    draw_gaussian_distribution_graph(flip_coin())
