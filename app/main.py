from random import randint


def flip_coin() -> dict:
    coin_flip_statistics = {}

    for amount in range(11):
        thousand_amount = 0

        for _ in range(10000):
            ten_amount = 10

            for _ in range(10):
                flip = randint(0, 1)
                if not flip:
                    ten_amount -= 1

            if ten_amount == amount:
                thousand_amount += 1

        coin_flip_statistics[amount] = thousand_amount / 10000 * 100

    return coin_flip_statistics
