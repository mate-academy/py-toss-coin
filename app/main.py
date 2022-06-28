from random import choice
import matplotlib.pyplot as plt


def flip_coin():
    coin = ["head", "tail"]
    results = []
    for _ in range(10000):
        count_head = 0
        for _ in range(10):
            flip = choice(coin)
            if flip == "head":
                count_head += 1
        results.append(count_head)
    temp_dict = {}
    for result in results:
        if result not in temp_dict:
            temp_dict[result] = 1
        else:
            temp_dict[result] += 1
    res_dict = {key: round((value / 10000) * 100, 2)
                for (key, value) in temp_dict.items()}
    res_dict = {key: res_dict[key] for key in sorted(res_dict)}
    return res_dict


def draw_gaussian_distribution_graph():
    plt.axis([0, 10, 0, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    x = list(flip_coin().keys())
    y = list(flip_coin().values())
    plt.plot(x, y)
    plt.show()
