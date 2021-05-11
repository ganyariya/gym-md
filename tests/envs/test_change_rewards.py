import pytest
from gym_md.envs.md_env import MdEnvBase


def test_change_rewards(make_gym: MdEnvBase):
    # test.json
    KILL = 4
    assert make_gym.setting.REWARDS["KILL"] == KILL

    rewards = {
        "TURN": -1,
        "EXIT": -1,
        "KILL": -1,
        "TREASURE": -1,
        "PORTION": -1,
        "DEAD": -1
    }
    make_gym.change_reward_values(rewards)

    # check setting memory-id
    assert make_gym.setting.REWARDS["KILL"] == -1
    assert make_gym.grid.setting.REWARDS["KILL"] == -1
    assert make_gym.agent.path.setting.REWARDS["KILL"] == -1

    # restore
    make_gym.restore_reward_values()
    assert make_gym.setting.REWARDS["KILL"] == KILL
    assert make_gym.grid.setting.REWARDS["KILL"] == KILL
    assert make_gym.agent.path.setting.REWARDS["KILL"] == KILL

    assert id(make_gym.setting.REWARDS) == id(make_gym.grid.setting.REWARDS)
