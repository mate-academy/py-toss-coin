from numpy import random


def flip_coin(num_experiments=10000) -> dict:
    statistics = {i: 0 for i in range(11)}  # Створюємо словник для підрахунку випадків від 0 до 10 орлів

    for _ in range(num_experiments):
        result = random.binomial(n=10, p=0.5)  # Підкидання 10 монет за один експеримент
        statistics[result] += 1  # Збільшуємо кількість для отриманого результату

    # Обчислюємо відсотки для кожної кількості орлів
    percentages = {key: (value / num_experiments) * 100 for key, value in statistics.items()}

    return percentages


print(flip_coin())
