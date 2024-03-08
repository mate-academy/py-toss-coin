import matplotlib.pyplot as plt
from random import randint

flip_dict, result_dict = {}, {}
times = 10_000


def flip_coin() -> dict:
    for i in range(times):
        flip_head = 0
        for count_flip in range(10):
            if randint(0, 1) == 1:
                flip_head += 1
            if flip_head not in flip_dict.keys():
                flip_dict[flip_head] = 0
        else:
            flip_dict[flip_head] += 1

    for key, value in flip_dict.items():
        flip_dict[key] = round(value / times * 100, 2)

    return dict(sorted(flip_dict.items()))


def draw_gaussian_distribution_graph() -> None:
    flip_res = flip_coin()
    xpoints = list(flip_res.keys())
    ypoints = list(flip_res.values())

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distributions")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
