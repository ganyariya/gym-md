from gym_md.envs.config.rewards_config import RewardsConfig
from gym_md.envs.config.props_config import PropsConfig


class TestConfig:
    def test_rewards_config(self) -> None:
        data = {
            "TURN": 10,
            "EXIT": 20,
            "KILL": 30,
            "TREASURE": 40,
            "POTION": 50,
            "DEAD": 60
        }
        rewards_config = RewardsConfig(**data)
        assert rewards_config.TURN == 10

    def test_props_config(self) -> None:
        data = {
            "PLAYER_MAX_HP": 40,
            "IS_PLAYER_HP_LIMIT": True,
            "ENEMY_POWER": 10,
            "ENEMY_POWER_MIN": 5,
            "ENEMY_POWER_MAX": 15,
            "IS_ENEMY_POWER_RANDOM": True,
            "POTION_POWER": 10,
            "DISTANCE_INF": 1000,
            "RENDER_WAIT_TIME": 0.05,
            "REWARDS":
                {
                    "TURN": 10,
                    "EXIT": 20,
                    "KILL": 30,
                    "TREASURE": 40,
                    "POTION": 50,
                    "DEAD": 60
                }
        }
        props_config = PropsConfig(**data)

        for k, v in data.items():
            assert getattr(props_config, k) == v

    def test_default_props_config(self) -> None:
        data = {
            "PLAYER_MAX_HP": 40,
            "ENEMY_POWER": 10,
            "POTION_POWER": 10,
            "DISTANCE_INF": 1000,
            "RENDER_WAIT_TIME": 0.05,
            "REWARDS":
                {
                    "TURN": 10,
                    "EXIT": 20,
                    "KILL": 30,
                    "TREASURE": 40,
                    "POTION": 50,
                    "DEAD": 60
                }
        }
        props_config = PropsConfig(**data)
        assert not props_config.IS_PLAYER_HP_LIMIT
        assert not props_config.IS_ENEMY_POWER_RANDOM
        assert props_config.ENEMY_POWER_MIN == 10
        assert props_config.ENEMY_POWER_MAX == 10
