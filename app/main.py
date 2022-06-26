from random import choice
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin(cases_count):
    count = dict.fromkeys((keys for keys in range(0, 11)), 0)
    coin = ["head", "tail"]
    for case in range(cases_count // 5):
        head_counter = 0

        for flip in range(0, 10):
            if choice(coin) == "head":
                head_counter += 1

        if head_counter == 0:
            count[0] += 1

        count[head_counter] += head_counter

    for key, value in count.items():
        count[key] = round((value / cases_count) * 100, 3)

    return count


def draw_gaussian_distribution_graph():
    cases = 10000
    data = flip_coin(cases)
    numbers = [keys for keys in data]
    percent = [values for values in data.values()]

    fig, ax = plt.subplots()

    ax.axis([0, 10, 0, 100])
    ax.locator_params(nbins=10)
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
    ax.set_title('Gaussian distribution')
    ax.set_xlabel('Heads count')
    ax.set_ylabel('Drop percentage %')
    ax.plot(numbers, percent, color="blue", linestyle='solid')
    fig.savefig("Gaussian distribution")
