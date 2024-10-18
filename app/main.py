import random
import matplotlib.pyplot as plt

def flip_coin() -> dict:
    scrim = ["head", "back"]
    result = {num: 0 for num in range(11)}

    for _ in range(10000):
        head_count = sum(1 for _ in range(10) if random.choice(scrim) == "head")
        result[head_count] += 1

    for key in result.keys():
        result[key] = round(result[key] / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph(data: dict):
    x = list(data.keys())
    y = list(data.values())

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Distribution')

    plt.title('Distribution of Heads in 10 Coin Flips (10000 Experiments)')
    plt.xlabel('Number of Heads')
    plt.ylabel('Percentage')

    plt.grid(True)

    plt.legend()

    plt.show()
