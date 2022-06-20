import random
import matplotlib.pyplot as plt


def flip_coin():
    case = ["head", "tail"]
    result_list = []
    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            result = random.choice(case)
            if result == "head":
                head_count += 1

        result_list.append(head_count)

    results = {key: 0 for key in range(0, 11)}

    for result in result_list:
        results[result] += 1

    for key, items in results.items():
        results[key] = round(items / 10000 * 100, 2)

    return results


def draw_gaussian_distribution_graph():
    x = [x for x in flip_coin().keys()]
    y = [y for y in flip_coin().values()]
    plt.plot(x, y)
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.title("Gaussian distribution")
    plt.xlim([0, max(x)])
    plt.ylim([0, 100])
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
