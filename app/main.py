from matplotlib import pyplot as plt
from pprint import pprint
from random import choice


def head_fell_out(number_of_flips: int) -> list:
    return [
        head
        for head in range(number_of_flips)
        if choice((0, 1)) == 0
    ]


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(*zip(*data.items()))
    plt.title("Gaussian distribution", fontsize=20)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.ylabel("Drop percentage %", fontsize=10)
    plt.xlabel("Heads count", fontsize=10)
    plt.show()


def flip_coin(number_of_flips: int,
              number_of_times: int,
              plot: bool = False) -> dict:
    percentages_of_head_fell_out = {}
    for _ in range(number_of_times):
        number_of_heads_fall_out = len(head_fell_out(number_of_flips))
        percentages_of_head_fell_out[
            number_of_heads_fall_out] = percentages_of_head_fell_out.get(
            number_of_heads_fall_out, 0) + 1

    for k, v in percentages_of_head_fell_out.items():
        percentages_of_head_fell_out[k] = round((v / number_of_times) * 100, 2)

    percentages_of_head_fell_out_keys = list(
        percentages_of_head_fell_out.keys()
    )
    percentages_of_head_fell_out_sorted = {
        k: percentages_of_head_fell_out[k]
        for k in sorted(percentages_of_head_fell_out_keys)
    }

    if plot:
        draw_gaussian_distribution_graph(percentages_of_head_fell_out_sorted)
        return percentages_of_head_fell_out_sorted
    return percentages_of_head_fell_out_sorted


if __name__ == '__main__':
    pprint(flip_coin(10, 10000, plot=True))
