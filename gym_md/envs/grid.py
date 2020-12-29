from typing import List, Tuple, Union

import numpy as np

from .point import Point


class Grid:

    def __init__(self, stage_file_path: str) -> None:
        self.H: int
        self.W: int
        self.g: List[List[int]]
        self.stage_file_path: str = stage_file_path

    def __getitem__(self, p: Point) -> int:
        y, x = p.y, p.x
        return self.g[y][x]

    def __setitem__(self, key: Point, value: int) -> None:
        y, x = key.y, key.x
        self.g[y][x] = value

    def _set_grid(self) -> None:
        with open(self.stage_file_path, 'r') as f:
            texts = [s.strip() for s in f]
        self.H = len(texts)
        self.W = len(texts[0])
