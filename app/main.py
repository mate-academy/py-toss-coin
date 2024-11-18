import random
import matplotlib.pyplot as plt


def flip_coin(num_of_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_of_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: round((v / num_of_cases) * 100, 2) for k, v in results.items()}
    return percentages

print(flip_coin())


def draw_gaussian_distribution_graph(data: dict):
    x = list(data.keys())
    y = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue', edgecolor='black')
    plt.plot(x, y, color='red', marker='o', linestyle='dashed', label='Gaussian Approximation')

    plt.xlabel('Heads count')
    plt.ylabel(' Drop percentage %')
    plt.title('Gaussian distribution')
    plt.xticks(range(0, 11))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    plt.show()