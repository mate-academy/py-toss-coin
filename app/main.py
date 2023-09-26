import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key, value in results.items():
        results[key] = (value / num_cases) * 100

    return results


def draw_gaussian_distribution_graph() -> None:
    graph = flip_coin()
    graph_x = list(graph.keys())
    graph_y = list(graph.values())

    plt.bar(graph_x, graph_y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.title("Gaussian distribution")

    plt.show()
