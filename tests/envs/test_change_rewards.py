import pytest
from gym_md.envs.md_env import MdEnvBase


def test_change_rewards(make_gym: MdEnvBase):
    # test.json
    assert make_gym.setting.REWARDS["KILL"] == 4

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
