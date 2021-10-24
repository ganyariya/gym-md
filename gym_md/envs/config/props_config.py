"""基本設定."""

from gym_md.envs.config.rewards_config import RewardsConfig
from pydantic import BaseModel


class PropsConfig(BaseModel):
    """基本設定."""

    PLAYER_MAX_HP: int
    ENEMY_POWER: int
    PORTION_POWER: int
    DISTANCE_INF: int
    RENDER_WAIT_TIME: float

    REWARDS: RewardsConfig
