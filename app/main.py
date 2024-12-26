import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts_of_experiments = 100000
    count_of_heads = {amount: 0 for amount in range(11)}

    for attempt in range(counts_of_experiments):
        heads = sum(random.choice([1, 0]) for flip in range(10))
        count_of_heads[heads] += 1

    count_of_heads_percent = {items: round((count
                              / counts_of_experiments) * 100, 2)
                              for items, count in count_of_heads.items()}

    return count_of_heads_percent


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    axis_x = list(data.keys())
    axis_y = list(data.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.plot(axis_x, axis_y, color="blue")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()


draw_gaussian_distribution_graph()
