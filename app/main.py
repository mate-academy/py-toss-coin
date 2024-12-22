import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    coin_side = ["head", "tail"]

    for _ in range(10_000):  # 10,000 экспериментов
        # Подсчет количества "head" за 10 бросков
        heads = sum(random.choice(coin_side) == "head" for _ in range(10))
        if heads in result:
            result[heads] += 1
        else:
            result[heads] = 1

    # Вычисление процентов
    percentages = {key: round((value / 10_000) * 100, 2) for key, value in result.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict):
    # Extract keys and values from the data
    x_values = sorted(data.keys())  # Number of heads (0 to 10)
    y_values = [data[key] for key in x_values]  # Corresponding percentages

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue', label="Distribution")

    # Add labels, title, and grid
    plt.title("Gaussian Distribution of Heads in 10 Flips", fontsize=16)
    plt.xlabel("Number of Heads", fontsize=14)
    plt.ylabel("Percentage (%)", fontsize=14)
    plt.xticks(range(min(x_values), max(x_values) + 1))  # Set x-axis ticks to integers
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)

    # Show the graph
    plt.show()


# Вывод и визуализация
flip_coin_dict = flip_coin()
print(flip_coin_dict)
draw_gaussian_distribution_graph(flip_coin_dict)
