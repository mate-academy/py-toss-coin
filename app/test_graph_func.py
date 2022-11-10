import os
from main import draw_gaussian_distribution_graph


def test_graph_coins_func():
    draw_gaussian_distribution_graph()
    assert os.path.exists(r"C:\Users\Dede\pythonProjects\py-flip-coin\app\graph.png") is True
