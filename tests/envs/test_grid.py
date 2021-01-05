import pytest

from gym_md.envs.grid import Grid
from gym_md.envs.setting import Setting


@pytest.fixture
def make_grid():
    name = 'test'
    setting = Setting(stage_name=name)
    grid = Grid(stage_name=name, setting=setting)
    return grid


def test_read_grid_as_list_from_stage_name(make_grid):
    assert True
