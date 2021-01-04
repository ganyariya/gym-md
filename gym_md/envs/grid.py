from typing import List, Tuple, Final
from os import path

from gym_md.envs.point import Point
from gym_md.envs.setting import Setting


class Grid:
    """

    Support grid information used by env.

    Attributes
    ----------
    setting: Setting
        settings
    H: int
        height
    W: int
        width
    g: list[list]
        information of each grid

    """

    def __init__(self, stage_name: str, setting: Setting) -> None:
        texts = Grid.read_grid_as_list(stage_name)
        self.setting: Final[Setting] = setting
        self.H: Final[int] = len(texts)
        self.W: Final[int] = len(texts[0])
        self.g: Final[List[List[int]]] = [[0] * self.W for _ in range(self.H)]
        for i in range(self.H):
            for j in range(self.W):
                self[i, j] = self.setting.CHARACTER_TO_NUM[texts[i][j]]

    def __getitem__(self, t: Point) -> int:
        y, x = t
        return self.g[y][x]

    def __setitem__(self, t: Point, value: int) -> None:
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


if __name__ == '__main__':
    stage_name: str = 'test'
    setting = Setting(stage_name=stage_name)
    grid = Grid(stage_name=stage_name, setting=setting)
