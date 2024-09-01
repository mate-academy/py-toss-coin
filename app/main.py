import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    all_cases = []
    res = {}
    for i in range(cases):
        heads = 0
        for i in range(10):
            flip = random.choice(["head", "tail"])
            if flip == "head":
                heads += 1
        all_cases.append(heads)
    for i in range(11):
        res[i] = all_cases.count(i) / cases * 100

    return res


def draw_gaussian_distribution_graph(data: dict) -> None:
    x = list(data.keys())
    y = list(data.values())
    
    # Plot the data
    plt.plot(x, y, color='red')
    plt.xlabel('Number of Heads')
    plt.ylabel('Percentage, %')
    plt.show()

print(flip_coin())
draw_gaussian_distribution_graph(flip_coin())
