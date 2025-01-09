import random
import matplotlib.pyplot as plt

def flip_once():
    heads_count = 0
    for _ in range(10):
        if random.choice([0, 1]) == 1:
            heads_count += 1
    return heads_count

def flip_experiment(trials=10000):
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = flip_once()
        results[heads_count] += 1
    percentages = {k: (v / trials) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph(data):
    x = list(data.keys())
    y = list(data.values())
    max_value = max(y)
    y_scaled = [(value / max_value) * 25 for value in y]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y_scaled, color='blue', marker='o', markersize=0)
    plt.title("Gaussian distribution", fontsize=16)
    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Drop percentage %", fontsize=12)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xticks(x)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

data = flip_experiment()
draw_gaussian_distribution_graph(data)