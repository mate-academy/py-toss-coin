import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    choice = [True, False]

    data_dictionary = {}

    for _ in range(10_000):
        heads = [random.choice(choice) for _ in range(10)]

        data_dictionary[heads.count(True)] = \
            data_dictionary.get(heads.count(True), 0) + 1

    data_dictionary = {x: y / 100 for x, y in data_dictionary.items()}
    sorted_d = dict(sorted(data_dictionary.items(), key=lambda x: x[0]))
    return sorted_d


def draw_gaussian_distribution_graph() -> None:
    percentages = flip_coin()
    num_heads = list(percentages.keys())
    probabilities = list(percentages.values())

    # Plot the distribution
    plt.bar(num_heads, probabilities)

    # Set labels and title
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")

    # Show the plot
    plt.show()
