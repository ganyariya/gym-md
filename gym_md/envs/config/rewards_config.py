"""Rewards Config."""
from pydantic import BaseModel


class RewardsConfig(BaseModel):
    """報酬ファイルを読み込む。"""

    TURN: float
    EXIT: float
    KILL: float
    TREASURE: float
    POTION: float
    DEAD: float
