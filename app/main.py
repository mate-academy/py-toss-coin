from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin(counts: int, iteration: int):
    def create_gaussian_chart(toss_coin: dict):
        dpi = 150
        fig = plt.figure(dpi=dpi, figsize=(1024 / dpi, 768 / dpi))
        mpl.rcParams.update({'font.size': 14})
        plt.axis([0, counts, 0, 100])
        plt.title('Gaussian distribution')
        plt.xlabel('Heads count')
        plt.ylabel('Drop percentage %')
        x_dots = []
        y_dots = []
        for x, y in enumerate(toss_coin.values()):
            y_dots.append(y)
            x_dots.append(x)
        plt.plot(x_dots, y_dots, color='blue', linestyle='solid',
                 label='gauss')
        plt.legend(loc='upper right')
        fig.savefig('gauss.png')

    result_dict = {}
    for _ in range(iteration):
        one, zero = 0, 0
        for _ in range(counts):
            if randint(0, 1):
                one += 1
            else:
                zero += 1
        if zero in result_dict:
            result_dict[zero] += 1
        else:
            result_dict[zero] = 1

    result = {key: round(value / iteration * 100, 2) for key, value in
              sorted(result_dict.items())}
    create_gaussian_chart(result)
    return result
