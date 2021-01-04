from queue import Queue
from typing import Final, List, Tuple, Dict
from gym_md.envs.grid import Grid
from gym_md.envs.setting import Setting
from gym_md.envs.point import Point
from gym_md.envs.agent.move_info import MoveInfo

DY: Final[Tuple[int, int, int, int]] = (0, 1, 0, -1)
DX: Final[Tuple[int, int, int, int]] = (1, 0, -1, 0)


class Path:

    def __init__(self, grid: Grid, setting: Setting):
        self.grid: Final[Grid] = grid
        self.setting: Final[Setting] = setting

    def get_moveinfo(self, y: int, x: int, safe: bool) -> MoveInfo:
        """
        座標(y, x)においてsafeのような移動をするときに
        次に進むべき座標の辞書を返す

        Parameters
        ----------
        y: int
        x: int
        safe: bool

        Returns
        -------
        move_info: dict of (str, (int, int))
            最も近い各タイルまで向かうために，次に進むべき1マスの座標の辞書

        """
        dist_and_prev: Final[Tuple[List[List[int]], List[List[Point]]]] = self.__get_distance_and_prev(y=y, x=x, safe=safe)
        dist: Final[List[List[int]]] = dist_and_prev[0]
        prev: Final[List[List[Point]]] = dist_and_prev[1]
        nearest_info: Final[Dict[str, Point]] = self.__get_nearest_info(dist)
        move_info = self.__calc_moveinfo(y, x, prev, nearest_info)
        return move_info

    def __calc_moveinfo(self, y: int, x: int, prev: List[List[Point]], nearest_info: Dict[str, Point]) -> MoveInfo:
        """

        Parameters
        ----------
        y: int
        x: int
        prev: list of list of tuple of int
        nearest_info: dict of (str, (int, int))

        Returns
        -------
        move_info: dict of (str, (int, int))
            最も近い各タイルまで向かうために，次に進むべき1マスの座標の辞書
        """
        move_info: Final[MoveInfo] = {c: (-1, -1) for c in self.setting.GRID_CHARACTERS}

        for gtype, pos in nearest_info.values():
            # gtypeのタイルが存在しない
            if pos == (-1, -1):
                continue
            py, px = pos
            while True:
                ny, nx = prev[py][px]
                if ny == y and nx == x:
                    break
                py, px = ny, nx
            move_info[gtype] = (py, px)

        return move_info

    def __get_distance_and_prev(self, y: int, x: int, safe: bool) \
            -> Tuple[List[List[int]], List[List[Point]]]:
        """

        座標(y, x)を初期位置としたときの
        他のマスまでの距離と前のマスを計算する

        Parameters
        ----------
        y: int
        x: int
        safe: bool

        Returns
        -------
        dist: list of list of int
        prev: list of list of tuple of int

        """
        H: Final[int] = self.grid.H
        W: Final[int] = self.grid.W
        INF: Final[int] = self.setting.DISTANCE_INF
        bad: Final[List[int]] = [self.setting.CHARACTER_TO_NUM['#']]
        if safe:
            bad.append(self.setting.CHARACTER_TO_NUM['M'])

        dist: Final[List[List[int]]] = [[INF for _ in range(W)] for _ in range(H)]
        prev: Final[List[List[Point]]] = [[(-1, -1) for _ in range(W)] for _ in range(H)]
        dist[y][x] = 0

        Q: Final[Queue] = Queue()
        Q.put((y, x))

        while not Q.empty():
            y, x = Q.get()
            for k in range(4):
                to_y = y + DY[k]
                to_x = x + DX[k]
                if Path.is_out(to_y, to_x, H, W):
                    continue
                if self.grid[to_y, to_x] in bad:
                    continue
                if dist[to_y][to_x] == INF:
                    dist[to_y][to_x] = dist[y][x] + 1
                    prev[to_y][to_x] = (y, x)
                    Q.put((to_y, to_x))

        return dist, prev

    def __get_nearest_info(self, dist: List[List[int]]) \
            -> Dict[str, Point]:
        """

        Parameters
        ----------
        dist: list of list of int
            各マスまでの距離

        Returns
        -------
        nearest_info: dict of tuple of (str, (int, int))
            初期位置から特定のタイルまでに最も近い位置を計算した辞書

        """
        nearest_info: Final[Dict[str, Point]] = {c: (-1, -1) for c in self.setting.GRID_CHARACTERS}
        for i in range(self.grid.H):
            for j in range(self.grid.W):
                gtype = self.setting.NUM_TO_CHARACTER[self.grid[i, j]]
                if nearest_info[gtype] == (-1, -1):
                    nearest_info[gtype] = (i, j)
                    continue
                nearest_info[gtype] = min(nearest_info[gtype], (i, j), key=lambda p: dist[p[0]][p[1]])
        return nearest_info

    @staticmethod
    def is_out(y: int, x: int, h: int, w: int) -> bool:
        return not (0 <= y < h and 0 <= x < w)
