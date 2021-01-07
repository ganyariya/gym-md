import pytest

from gym_md.envs.setting import Setting

NAME = 'test'


def test_json_load(make_setting: Setting):
    assert make_setting.STAGE_NAME == NAME
    assert make_setting.REWARDS['KILL'] == 4
    assert make_setting.PLAYER_MAX_HP == 30
