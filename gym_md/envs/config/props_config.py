"""基本設定."""

from pydantic import BaseModel

from gym_md.envs.config.rewards_config import RewardsConfig


class PropsConfig(BaseModel):
    """基本設定."""

    PLAYER_MAX_HP: int = 40
    IS_PLAYER_HP_LIMIT: bool = False

    ENEMY_POWER: int = 10
    # [l, r]
    ENEMY_POWER_MIN: int = 10
    ENEMY_POWER_MAX: int = 10
    IS_ENEMY_POWER_RANDOM: bool = False

    POTION_POWER: int = 10
    DISTANCE_INF: int
    RENDER_WAIT_TIME: float

    REWARDS: RewardsConfig
