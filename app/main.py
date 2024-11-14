import random
import matplotlib.pyplot as plt


def flip_coin() -> dict :
    flip_results = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        flip_results[heads_count] += 1

    for key in flip_results:
        flip_results[key] = int((flip_results[key] / num_trials) * 100)

    return flip_results


def draw_gaussian_distribution_graph(flip_results: dict) -> None:
    labels = list(flip_results.keys())
    values = list(flip_results.values())

    plt.bar(labels, values, color="blue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.show()


# Example usage
f_results = flip_coin()
print(f_results)
draw_gaussian_distribution_graph(f_results)
