import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    num_trials = 10_000

    for _ in range(num_trials):
        num_heads = 0
        for _ in range(10):
            if random.random() <= 0.5:
                num_heads += 1
        results[num_heads] += 1

    distribution = {k: v / num_trials * 100 for k, v in results.items()}

    return distribution


def draw_gaussian_distribution_graph() -> None:
    x_axes = flip_coin().keys()
    y_axes = flip_coin().values()
    plt.style.use("bmh")
    fig, ax = plt.subplots()
    ax.axis([0, 10, 0, 100])
    ax.plot(x_axes, y_axes)
    ax.set_xticks(range(0, 11, 1))
    ax.set_yticks(range(0, 101, 10))
    ax.set_title("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")
    plt.show()
