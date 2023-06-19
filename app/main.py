from random import choice
from matplotlib import pyplot


def flip_coin() -> dict:
    result = {i: 0 for i in range(10)}

    for _ in range(10000):
        heads = 0

        for _ in range(10):
            if choice(("head", "tail")) == "head":
                heads += 1
        result[heads] = result.get(heads, 0) + 1

    total_cases = sum(result.values())
    percentages = {
        head: round((count / total_cases) * 100, 2)
        for head, count in result.items()
    }

    return percentages


def draw_gaussian_distribution_graph(result: dict) -> None:
    heads_dropped = list(result.keys())
    percentages = list(result.values())

    pyplot.plot(heads_dropped, percentages, marker="o")
    pyplot.xlabel("Heads Count")
    pyplot.ylabel("Drop Percentage %")
    pyplot.title("Gaussian Distribution")
    pyplot.xticks(heads_dropped)
    pyplot.yticks(range(0, 100 + 1, 10))
    pyplot.show()


draw_gaussian_distribution_graph(flip_coin())
