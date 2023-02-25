import matplotlib.pyplot as plt


def draw_gaussian_distribution_graph(dct_stat: dict) -> None:
    heads_count = list(dct_stat.values())
    dpop_pers = list(dct_stat.keys())
    plt.plot(dpop_pers, heads_count)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian distribution")
    plt.show()