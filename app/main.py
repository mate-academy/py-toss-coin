import random
import matplotlib.pyplot as plt


def flip_coin(num_trials=10000):
    results = {}
    for i in range(num_trials):
        num_heads = 0
        for j in range(10):
            if random.random() < 0.5:
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1
    for k in results:
        results[k] = 100.0 * results[k] / num_trials
    return results


def draw_gaussian_distribution_graph(results):
    x = []
    y = []
    for k in range(11):
        x.append(k)
        if k in results:
            y.append(results[k])
        else:
            y.append(0)
    plt.plot(x, y, 'bo')
    plt.xlabel('Number of Heads')
    plt.ylabel('Percentage')
    plt.title('Coin Flips')
    plt.show()

