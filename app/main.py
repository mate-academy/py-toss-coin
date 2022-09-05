import random
import matplotlib.pyplot as plt


def flip_coin(count: int = 10000):
    result_dict = dict.fromkeys([number for number in range(0, 11)], 0)
    coin = ["heads", "tails"]
    count_list = []

    for _ in range(count):
        total_heads = 0
        for _ in range(0, 10):
            if random.choice(coin) == "heads":
                total_heads += 1
        count_list.append(total_heads)

    for number in range(0, 11):
        value = (count_list.count(number) / 10000) * 100
        result_dict[number] = value

    return result_dict


def draw_gaussian_distribution_graph():
    fig, ax = plt.subplots()
    data = flip_coin()

    # Adding labels and title
    ax.set_title("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")

    # Building graphic
    ax.plot(data.keys(), data.values())
    ax.grid()
