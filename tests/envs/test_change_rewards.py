import pytest
from gym_md.envs.md_env import MdEnvBase


def test_change_rewards(make_gym: MdEnvBase):
    # test.json
    KILL = 4
    assert make_gym.setting.REWARDS.KILL == KILL

    rewards = {
        "TURN": 10,
        "EXIT": -1,
        "KILL": -1,
        "TREASURE": -1,
        "POTION": -1,
        "DEAD": -1
    }
    make_gym.change_reward_values(rewards)

    # check setting memory-id
    assert make_gym.setting.REWARDS.KILL == -1
    assert make_gym.grid.setting.REWARDS.KILL == -1
    assert make_gym.agent.path.setting.REWARDS.KILL == -1
    assert make_gym.setting.REWARDS.TURN == 10
    assert make_gym.grid.setting.REWARDS.TURN == 10
    assert make_gym.agent.path.setting.REWARDS.TURN == 10

    rewards = {
        "TURN": 101,
        "EXIT": 102,
        "KILL": 103,
        "TREASURE": 104,
        "POTION": 105,
        "DEAD": 106
    }
    make_gym.change_reward_values(rewards)
    for key, value in rewards.items():
        assert getattr(make_gym.setting.REWARDS, key) == value
        assert getattr(make_gym.grid.setting.REWARDS, key) == value
        assert getattr(make_gym.agent.setting.REWARDS, key) == value
        assert getattr(make_gym.agent.path.setting.REWARDS, key) == value
        assert getattr(make_gym.agent.grid.setting.REWARDS, key) == value
        assert getattr(make_gym.agent.actioner.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.grid.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.agent.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.generator.agent.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.generator.grid.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.generator.agent.grid.setting.REWARDS, key) == value
        assert getattr(make_gym.renderer.generator.agent.actioner.setting.REWARDS, key) == value

        # restore
    make_gym.restore_reward_values()
    assert make_gym.setting.REWARDS.KILL == KILL
    assert make_gym.grid.setting.REWARDS.KILL == KILL
    assert make_gym.agent.path.setting.REWARDS.KILL == KILL

    assert id(make_gym.setting.REWARDS) == id(make_gym.grid.setting.REWARDS)
    assert id(make_gym.setting.REWARDS) == id(make_gym.agent.path.setting.REWARDS)