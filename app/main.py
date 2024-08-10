import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_simulations = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(number_of_simulations):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / number_of_simulations) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    keys = list(results.keys())
    values = list(results.values())

    plt.plot(keys, values)

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian distribution")

    plt.show()


draw_gaussian_distribution_graph()
