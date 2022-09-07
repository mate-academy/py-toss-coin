import random
import matplotlib.pyplot as plt


def flip_ten_times():
    """Flip coin 10 times and return how many times was heads"""
    heads = []
    for _ in range(10):
        coin_side = random.choice(["head", "tail"])
        heads.append(1) if coin_side == "head" else heads.append(0)
    return sum(heads)


def flip_coin():
    percentage_dict = {}
    flip_times = 10000
    """We try some amount of times to flip coin
     of 10 times with purpose to check distribution"""
    for _ in range(flip_times):
        head_flip_ten = flip_ten_times()
        if percentage_dict.get(head_flip_ten):
            percentage_dict[head_flip_ten] += 1
        else:
            percentage_dict[head_flip_ten] = 1
    percentage_dict = {key: value / flip_times * 100
                       for key, value in sorted(percentage_dict.items())}

    # we prepare data for plotting
    x = [i for i in percentage_dict.keys()]
    y = [i for i in percentage_dict.values()]

    fig, ax = plt.subplots()
    ax.plot(x, y, color='b', linewidth=1)
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 10)
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")
    ax.set_title("Gaussian distribution")
    plt.show()

    return percentage_dict
