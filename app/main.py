import random
import matplotlib.pyplot as plt


def flip_coin(num_simulations=10000, num_flips=10):
    results = {k: 0 for k in range(num_flips + 1)}
    
    for _ in range(num_simulations):
        flips = [random.choice(['H', 'T']) for _ in range(num_flips)]
        num_heads = flips.count('H')
        results[num_heads] += 1
    
    for k in results:
        results[k] = (results[k] / num_simulations) * 100
    
    return results


def draw_gaussian_distribution_graph(data):
    keys = list(data.keys())
    values = list(data.values())
    
    plt.bar(keys, values)
    plt.xlabel('Number of Heads')
    plt.ylabel('Percentage')
    plt.title('Distribution of Heads in 10 Coin Flips over 10,000 Simulations')
    plt.show()


data = flip_coin()
print(data)
draw_gaussian_distribution_graph(data)
