import os
from typing import Any
from pathlib import Path

from main import draw_gaussian_distribution_graph


BASE_DIR = Path(__file__).resolve().parent.parent

GRAPH = f"{BASE_DIR}/graph.png"


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


def test_graph_coins_func() -> None:
    with CleanUpFile(GRAPH):
        draw_gaussian_distribution_graph()
        assert (
            os.path.exists(f"{BASE_DIR}/graph.png") is True
        ), "Function should draw graph"
