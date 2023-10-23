import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count = 0
    coin_flip_count = 0
    temp_list = []
    result_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    while count != 1_00_000:
        coin_flip_count += 1
        count += 1
        coin = random.choice([0, 1])
        temp_list.append(coin)
        if coin_flip_count == 10:
            coin_flip_count = 0
            temp_count = temp_list.count(1)
            result_dict[temp_count] += 1
            temp_list = []

    for key, value in result_dict.items():
        result_dict[key] = round(100 / (10_000 / value), 2)

    return result_dict


def draw_gaussian_distribution_graph(data_dict: dict) -> None:

    x_values = []
    y_values = []

    for key, value in data_dict.items():
        x_values.append(key)
        y_values.append(value)

    plt.plot(x_values, y_values)

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(11))

    plt.title("Coin flip probability diagram")
    plt.xlabel("Count of flips by 10 times")
    plt.ylabel("Probability percent")

    plt.show()


dict_fot_table = flip_coin()

draw_gaussian_distribution_graph(dict_fot_table)
