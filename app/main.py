import random
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        num_heads = sum(random.randint(0, 1) for _ in range(num_flips))
        results[num_heads] += 1

    return {
        key: (value / num_cases * 100)
        for key, value in results.items()
    }


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(data.keys(), data.values())
    plt.show()
