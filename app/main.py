import random


def flip_coin() -> dict:
    coin_side = ["H", "T"]
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        pre_result = []
        for _ in range(10):
            pre_result.append(random.choice(coin_side))
        sum_heads = pre_result.count("H")
        result[sum_heads] += 1

    total_cases = sum(result.values())
    percentages = {
        k: round(v / total_cases * 100, 2) for k, v in result.items()
    }
    return percentages

# def draw_gaussian_distribution_graph(percentage: dict) -> None:
#     result_list = []
#     for number in percentage.values():
#         result_list.append(int(number))
#     ypoints = np.array(result_list)
#
#     plt.plot(ypoints)
#     plt.ylim(0, 100)
#     plt.xlim(0, len(percentage) - 1)
#
#     x_ticks = np.arange(0, len(percentage))
#     y_ticks = np.arange(0, 101, 10)
#
#     plt.xlabel("Head count")
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#
#     plt.xticks(x_ticks)
#     plt.yticks(y_ticks)
#     plt.show()
#
#
# draw_gaussian_distribution_graph(flip_coin())
