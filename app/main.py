import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flipping_amount = 100_000
    results = {i: 0 for i in range(11)}

    for side in range(flipping_amount):
        heads = 0
        for flip in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / flipping_amount) * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    abscissa = list(results.keys())
    ordinate = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.plot(abscissa, ordinate, marker="o")
    plt.title("Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.grid(True)

    plt.savefig("gaussian_distribution.png")

    plt.show(block=True)


results = flip_coin()
draw_gaussian_distribution_graph(results)
