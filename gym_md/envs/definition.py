"""definition ."""
from typing import Final, List

GRID_CHARACTERS: Final[List[str]] = [
    ".",
    "#",
    "T",
    "P",
    "M",
    "E",
    "S",
    "A",
]
OBSERVATIONS: Final[List[str]] = [
    "MONSTER",
    "TREASURE",
    "TREASURE_SAFELY",
    "PORTION",
    "PORTION_SAFELY",
    "EXIT",
    "EXIT_SAFELY",
    "HP",
]
ACTIONS: Final[List[str]] = [
    "MONSTER",
    "TREASURE",
    "TREASURE_SAFELY",
    "PORTION",
    "PORTION_SAFELY",
    "EXIT",
    "EXIT_SAFELY",
]
CUSTOM_PROPS: Final[List[str]] = [
    "PLAYER_MAX_HP",
    "ENEMY_POWER",
    "PORTION_POWER",
    "DISTANCE_INF",
    "RENDER_WAIT_TIME",
    "REWARDS",
]
