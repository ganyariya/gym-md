from typing import Final

from gym_md.envs.point import Point
from gym_md.envs.grid import Grid
from gym_md.envs.setting import Setting
from gym_md.envs.agent.path import Path
from gym_md.envs.agent.actioner import Actioner, Actions
from gym_md.envs.agent.move_info import MoveInfo


class Agent:

    def __init__(self, grid: Grid, setting: Setting):
        self.grid: Final[Grid] = grid
        self.setting: Final[Setting] = setting
        self.path: Final[Path] = Path(grid=grid, setting=setting)
        self.actioner: Final[Actioner] = Actioner()
        self.y: int = -1
        self.x: int = -1

    def take_action(self, actions: Actions) -> int:
        info: Final[MoveInfo] = self.path.get_moveinfo(y=self.y, x=self.x, safe=False)
        safe_info: Final[MoveInfo] = self.path.get_moveinfo(y=self.y, x=self.x, safe=True)
        pass
