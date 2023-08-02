from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    head, tail = 1, 0
    tosses, trials = 10, 10000
    counts = {}
    for _ in range(trials):
        count = 0
        for _ in range(tosses):
            side = choice((head, tail))
            if side == head:
                count += 1
        if count not in counts:
            counts[count] = 0
        counts[count] += 1
    keys = sorted(counts.keys())
    return {
        index: round(((counts[index] / trials) * 100), 2)
        for index in keys
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    percents = [num for num in range(0, 101, 10)]
    plt.style.use('seaborn-v0_8')

    fig, ax = plt.subplots()
    ax.plot(percents, data.values(), linewidth=3)

    ax.set_title("Gaussian distribution", fontsize=24)
    ax.set_ylabel("Drop percentage %", fontsize=14)
    ax.set_xlabel("Heads count", fontsize=14)

    ax.tick_params(axis='both', labelsize=14)

    plt.show()


if __name__ == '__main__':
    draw_gaussian_distribution_graph(flip_coin())
