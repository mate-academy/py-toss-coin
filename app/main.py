import random
import matplotlib.pyplot as plt


def flip_coin(count: int = 10000):
    data_dict = dict.fromkeys([number for number in range(0, 11)], 0)
    flip_choice = ["heads", "tails"]
    result_list = []

    for _ in range(count):
        total_heads = 0
        for _ in range(0, 10):
            if random.choice(flip_choice) == "heads":
                total_heads += 1
        result_list.append(total_heads)

    for val in range(0, 11):
        value = (result_list.count(val) / 10000) * 100
        data_dict[val] = value

    return data_dict


def draw_gaussian_distribution_graph():
    fig, ax = plt.subplots()
    data = flip_coin()

    # Adding axis labels and title
    ax.settitle("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")

    # Building graph
    x = data.keys()
    y = data.values()
    ax.plot(x, y)
    ax.grid()
