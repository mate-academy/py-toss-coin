import random
import matplotlib.pyplot as plt


def imitate_coins_flip(cases: int) -> dict:
    result_dict = {}
    for _ in range(cases):
        head_drops = 0
        for i in range(10):
            is_heads = random.randint(0, 1)  # 1 - head
            if is_heads == 1:
                head_drops += 1

        if head_drops in result_dict:
            result_dict[head_drops] += 1
        else:
            result_dict[head_drops] = 1

    return {key: val for key, val in
            sorted(result_dict.items(), key=lambda ele: ele[0])}


def flip_coin() -> dict:
    cases = 10000
    result_dict = imitate_coins_flip(cases)

    for key in result_dict:
        result_dict[key] = round((result_dict[key] * 100) / cases, 2)
    return result_dict


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    cases = 10000
    result_dict = imitate_coins_flip(cases)
    plt.plot(result_dict.keys(), result_dict.values())
    plt.show()


# draw_gaussian_distribution_graph()
