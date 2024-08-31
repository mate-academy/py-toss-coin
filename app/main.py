import matplotlib.pyplot as plt
import random


def flip_coin(
    num_trials: int = 10000,
    num_flips: int = 10
) -> dict[int, float]:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    plt.plot(
        list(data.keys()),
        list(data.values()),
        color="blue"
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
