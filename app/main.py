import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    for i in range(10001):
        get_head_times = 0
        for flip in range(10):
            # flipping the cion 10 times
            flip_result = random.randrange(2)
            # 0 - head, count, how many times we have head
            if flip_result == 0:
                get_head_times += 1
        result[get_head_times] += 1
    for key, value in result.items():
        result[key] = value * 100 / 10000
    return result


def draw_gaussian_distribution_graph(func: dict) -> None:
    distribution = func
    percentage = distribution.values()
    plt.axis([0, 10, 0, 100])
    plt.plot(percentage)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
draw_gaussian_distribution_graph(flip_coin())