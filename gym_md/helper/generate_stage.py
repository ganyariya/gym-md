"""ステージを生成する."""
import bisect
import copy
import random
from os import path
from typing import List

import numpy as np

from gym_md.envs import definition


def roulette(weight: List[int]) -> int:
    """ルーレット選択を行う.

    Parameters
    ----------
    weight

    Returns
    -------
    int

    """
    total = sum(weight)
    c_sum = np.cumsum(weight)
    return bisect.bisect_left(c_sum, total * random.random())


characters = copy.deepcopy(definition.GRID_CHARACTERS)[:-3]

H: int = int(input("height: "))
W: int = int(input("width: "))
stage_name: str = input("stage_name: ").rstrip()
stages_dir: str = path.join(path.dirname(__file__), "..", "envs", "stages")
dp: List[List[str]] = [["?"] * W for _ in range(H)]

weight = [100, 60, 20, 20, 15]
for i in range(H):
    for j in range(W):
        dp[i][j] = characters[roulette(weight)]

for c in ["S", "E"]:
    while True:
        y = random.randint(0, H - 1)
        x = random.randint(0, W - 1)
        if dp[y][x] == "S":
            continue
        dp[y][x] = c
        break

with open(path.join(stages_dir, f"{stage_name}.txt"), "w") as f:
    for i in range(H):
        f.write("".join(dp[i]))
        if i < H - 1:
            f.write("\n")
