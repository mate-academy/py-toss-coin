import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    print(results)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    plt.bar(results.keys(), results.values(), tick_label=list(results.keys()))
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads")
    plt.grid(True)
    plt.show()


res = flip_coin()
print(res)
draw_gaussian_distribution_graph(res)
