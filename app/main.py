import random
import matplotlib.pyplot as plt


from matplotlib.ticker import AutoMinorLocator


def flip_coin() -> dict:
    result_dict = {}
    coin = ["Heads", "Tails"]
    for case in range(10000):
        count = 0
        for flip in range(10):
            if random.choice(coin) == "Heads":
                count += 1
        if count in result_dict:
            result_dict[count] += 1
            continue
        result_dict[count] = count
    for num_of_heads_drop, times_of_drop in result_dict.items():
        percent_of_drop = times_of_drop / 100
        result_dict[num_of_heads_drop] = percent_of_drop
    return {
        count_of_heads: result_dict[count_of_heads] for count_of_heads in
        sorted(sorted_keys for sorted_keys in result_dict.keys())
    }


def draw_gaussian_distribution_graph(result_dict: dict[flip_coin()]) -> None:
    x_ax = [item for item in result_dict.keys()]
    y_ax = [item for item in result_dict.values()]
    fig, ax = plt.subplots()
    ax.plot(x_ax, y_ax)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])
    plt.xticks(range(min(x_ax), max(x_ax) + 1, 1))
    plt.yticks(range(0, 101, 10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.show()
