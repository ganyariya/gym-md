from typing import List, Tuple, Final
from os import path

import numpy as np

from .settings import Settings


class Grid:
    """

    Support grid information used by env.

    Attributes
    ----------
    C: Settings
        settings
    H: int
        height
    W: int
        width
    g: list[list]
        information of each grid

    """

    def __init__(self, stage_name: str, const: Settings) -> None:
        texts = Grid.read_grid_as_list(stage_name)
        self.C: Final[Settings] = const
        self.H: int = len(texts)
        self.W: int = len(texts[0])
        self.g: List[List[int]] = [[0] * self.W for _ in range(self.H)]
        for i in range(self.H):
            for j in range(self.W):
                self[i, j] = self.C.CHARACTER_TO_NUM[texts[i][j]]

    def __getitem__(self, t: Tuple[int, int]) -> int:
        y, x = t
        return self.g[y][x]

    def __setitem__(self, t: Tuple[int, int], value: int) -> None:
        y, x = t
        self.g[y][x] = value

    @staticmethod
    def read_grid_as_list(stage_name: str) -> List[str]:
        """

        Read stage from stage name, and
        return texts as list[str].

        Parameters
        ----------
        stage_name: str


        Returns
        -------
        texts: list
        """
        stage_file = path.join('stages', f'{stage_name}.txt')
        with open(stage_file, 'r') as f:
            texts = [s.strip() for s in f]
        return texts
