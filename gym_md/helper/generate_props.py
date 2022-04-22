"""propを生成する."""
import json
import random
from os import path


def r(le: int, ri: int):
    """Generate random."""
    return random.randint(le, ri)


stage_name: str = input("stage_name: ").rstrip()
stages_dir: str = path.join(path.dirname(__file__), "..", "envs", "props")

PLAYER_MAX_HP = 40
ENEMY_POWER = 10
POTION_POWER = 10

TURN_MIN = 1
TURN_MAX = 5

EXIT_MIN = 10
EXIT_MAX = 30

KILL_MIN = 3
KILL_MAX = 8

TREASURE_MIN = 1
TREASURE_MAX = 6

POTION_MIN = 1
POTION_MAX = 4

DEAD_MIN = -30
DEAD_MAX = -10

dp = {
    "PLAYER_MAX_HP": PLAYER_MAX_HP,
    "ENEMY_POWER": ENEMY_POWER,
    "POTION_POWER": POTION_POWER,
    "DISTANCE_INF": 1000,
    "RENDER_WAIT_TIME": 0.05,
    "REWARDS": {
        "TURN": r(TURN_MIN, TURN_MAX),
        "EXIT": r(EXIT_MIN, EXIT_MAX),
        "KILL": r(KILL_MIN, KILL_MAX),
        "TREASURE": r(TREASURE_MIN, TREASURE_MAX),
        "POTION": r(POTION_MIN, POTION_MAX),
        "DEAD": r(DEAD_MIN, DEAD_MAX),
    },
}

with open(path.join(stages_dir, f"{stage_name}.json"), "w") as f:
    json.dump(dp, f, indent=2)
