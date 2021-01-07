"""agent module."""
from typing import Final

from gym_md.envs.agent.actioner import Actioner, Actions
from gym_md.envs.agent.move_info import MoveInfo
from gym_md.envs.agent.pather import Pather
from gym_md.envs.grid import Grid
from gym_md.envs.setting import Setting


class Agent:
    """Agent class.

    エージェントクラス．
    Pather, Actionerを持つ．

    """

    def __init__(self, grid: Grid, setting: Setting):
        self.grid: Final[Grid] = grid
        self.setting: Final[Setting] = setting
        self.path: Final[Pather] = Pather(grid=grid, setting=setting)
        self.actioner: Final[Actioner] = Actioner(setting=setting)
        self.y: int = -1
        self.x: int = -1

    def take_action(self, actions: Actions) -> int:
        info: Final[MoveInfo] = self.path.get_moveinfo(y=self.y, x=self.x, safe=False)
        safe_info: Final[MoveInfo] = self.path.get_moveinfo(
            y=self.y, x=self.x, safe=True
        )
        unsafe_info: Final[MoveInfo] = self.path.get_moveinfo(
            y=self.y, x=self.x, safe=False
        )
        selected_action = self.actioner.take_action(
            actions=actions, safe_info=safe_info, unsafe_info=unsafe_info
        )
