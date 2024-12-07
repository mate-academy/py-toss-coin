import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, float]:
    results = {}
    for i in range(11):
        results[i] = 0  # Инициализируем словарь с ключами от 0 до 10

    for _ in range(10000):  # Проводим 10000 случаев подбрасывания
        count_heads = 0
        for _ in range(10):  # Подбрасываем монету 10 раз
            if random.randint(0, 1) == 0:
                count_heads += 1
        results[count_heads] += 1

    # Переводим количество выпадений орлов в проценты
    for key in results:
        results[key] = (results[key] / 10000) * 100
    return results


def draw_gaussian_distribution_graph(results: dict[int, float]) -> plt.Figure:
    xpoints = np.array(list(results.keys()))
    ypoints = np.array(list(results.values()))

    plt.plot(xpoints, ypoints)
    plt.show()
