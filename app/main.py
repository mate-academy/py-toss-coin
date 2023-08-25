import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
              5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for __ in range(10000):
        count = 0
        for _ in range(10):
            count += random.randint(0, 1)
        if count == 0:
            result[count] += 1
        else:
            result[count] += 1
    for key, value in result.items():
        result[key] = round((value * 100 / 10000), 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    dict_of_numbers = flip_coin()
    x_coord = dict_of_numbers.keys()
    y_coord = dict_of_numbers.values()

    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    plt.plot(x_coord, y_coord)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
