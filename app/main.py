import random
import matplotlib.pyplot as plt


def percentage_conversion(amount: int) -> float:
    return amount * 100 / 10000


def flip_coin() -> dict:
    heads = []
    tails = []
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                   5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for count in range(10001):
        for i in range(10):
            coin = random.randint(0, 1)
            if coin == 0:
                heads.append(coin)
            if coin == 1:
                tails.append(coin)
        result_dict[len(heads)] += 1
        heads.clear()
    final_dict = {
        0: percentage_conversion(result_dict[0]),
        1: percentage_conversion(result_dict[1]),
        2: percentage_conversion(result_dict[2]),
        3: percentage_conversion(result_dict[3]),
        4: percentage_conversion(result_dict[4]),
        5: percentage_conversion(result_dict[5]),
        6: percentage_conversion(result_dict[6]),
        7: percentage_conversion(result_dict[7]),
        8: percentage_conversion(result_dict[8]),
        9: percentage_conversion(result_dict[9]),
        10: percentage_conversion(result_dict[10]),
    }
    return final_dict


def graphic(data: dict) -> None:
    x_points = [key for key in data]
    y_points = [value for key, value in data.items()]
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Head counts")
    plt.ylabel("Drop percentage, %")
    return plt.show()
