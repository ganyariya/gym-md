"""Grid Module.

マップの情報を格納するGridクラス

Notes
-----
Gridの要素を　画像や文字を管理したクラスに変更する

"""
from os import path
from typing import Final, List

from gym_md.envs.point import Point
from gym_md.envs.setting import Setting


class Grid:
    """Grid Class.

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
        self.texts: Final[List[str]] = Grid.read_grid_as_list_from_stage_name(
            stage_name
        )
        self.setting: Final[Setting] = setting
        self.H: Final[int] = len(self.texts)
        self.W: Final[int] = len(self.texts[0])
        self.g: Final[List[List[int]]] = [[0] * self.W for _ in range(self.H)]

        self.reset()

    def reset(self) -> None:
        """ステージのリセットをする."""
        for i in range(self.H):
            for j in range(self.W):
                self[i, j] = self.setting.CHARACTER_TO_NUM[self.texts[i][j]]

    def __getitem__(self, t: Point) -> int:
        """ある座標の状態を返す.

        Notes
        -----
        Pointはtuple(int, int)

        Returns
        -------
        int
        """
        y, x = t
        return self.g[y][x]

    def __setitem__(self, t: Point, value: int) -> None:
        """あるPointに要素を設定する.

        Parameters
        ----------
        t: Point
        value: int
        """
        y, x = t
        self.g[y][x] = value

    @staticmethod
    def read_grid_as_list_from_stage_name(stage_name: str) -> List[str]:
        """ステージ名からリストを返す.

        Read stage from stage name, and
        return texts as list[str].

        Parameters
        ----------
        stage_name: str


        Returns
        -------
        list
        """
        file_dir = path.dirname(__file__)
        stage_file = path.join(file_dir, "stages", f"{stage_name}.txt")
        with open(stage_file, "r") as f:
            texts = [s.strip() for s in f]
        return texts
