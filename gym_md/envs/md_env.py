from typing import Final, List
from collections import defaultdict
from PIL import Image
import gym

from gym_md.envs.agent.agent import Agent
from gym_md.envs.agent.actioner import Actions
from gym_md.envs.renderer.renderer import Renderer
from gym_md.envs.grid import Grid
from gym_md.envs.setting import Setting


class MdEnvBase(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self, stage_name: str):
        self.stage_name: Final[str] = stage_name
        self.setting: Final[Setting] = Setting(self.stage_name)
        self.grid: Grid = Grid(self.stage_name, self.setting)
        self.agent: Agent = Agent(self.grid, self.setting)
        self.renderer: Final[Renderer] = Renderer(self.grid, self.agent)
        self.info: defaultdict = defaultdict(int)

    def reset(self):
        self.grid = Grid(self.stage_name, self.setting)
        self.agent = Agent(self.grid, self.setting)
        self.info = defaultdict(int)

    def step(self, actions: Actions):
        action: Final[int] = self.agent.select_action(actions)
        self.agent.take_action(action)

    def render(self, mode="human") -> Image:
        return self.renderer.render(mode=mode)

    def generate(self, mode="human") -> Image:
        return self.renderer.generate(mode=mode)

    def close(self):
        self.reset()

    def _get_reward(self) -> int:
        R = self.setting.REWARDS
        C = self.setting.CHARACTER_TO_NUM
        ret: int = -R["TURN"]
        y, x = self.agent.y, self.agent.x
        if self.agent.hp <= 0:
            return ret + R["DEAD"]
        if self.grid[y, x] == C["T"]:
            ret += R["TREASURE"]
        if self.grid[y, x] == C["E"]:
            ret += R["EXIT"]
        if self.grid[y, x] == C["M"]:
            ret += R["KILL"]
        if self.grid[y, x] == C["P"]:
            ret += R["PORTION"]
        return ret

    def _get_observation(self) -> List[int]:
        s, _ = self.agent.path.get_distance_and_prev(
            y=self.agent.y, x=self.agent.x, safe=True
        )
        u, _ = self.agent.path.get_distance_and_prev(
            y=self.agent.y, x=self.agent.x, safe=False
        )
        # ここ面倒
