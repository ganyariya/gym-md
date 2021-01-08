import pytest

from gym_md.envs.agent.agent import Agent
from gym_md.envs.grid import Grid
from gym_md.envs.setting import Setting


@pytest.fixture
def make_agent(make_grid: Grid) -> Agent:
    setting: Setting = make_grid.setting
    agent: Agent = Agent(grid=make_grid, setting=setting)
    return agent
