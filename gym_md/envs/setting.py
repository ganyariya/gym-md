import json
from os import path
from typing import Dict, Final, List

from gym_md.envs.singleton import Singleton


class Setting(Singleton):
    """

    ステージに関する設定ファイル

    Attributes
    ----------
    STAGE_NAME: str
        the name of stage
    GRID_CHARACTERS: list of str
        characters representing each tile
    OBSERVATIONS: list of str
        observations of agent receiving from gym
    ACTIONS: list of str
        actions of agent giving to gym

    """

    def __init__(self, stage_name: str):
        self.STAGE_NAME: Final[str] = stage_name
        self.GRID_CHARACTERS: Final[List[str]] = [
            ".",
            "#",
            "T",
            "P",
            "M",
            "E",
            "S",
            "A",
        ]
        self.OBSERVATIONS: Final[List[str]] = [
            "MONSTER",
            "TREASURE",
            "TREASURE_SAFELY",
            "PORTION",
            "PORTION_SAFELY",
            "EXIT",
            "EXIT_SAFELY",
            "HP",
        ]
        self.ACTIONS: Final[List[str]] = [
            "MONSTER",
            "TREASURE",
            "TREASURE_SAFELY",
            "PORTION",
            "PORTION_SAFELY",
            "EXIT",
            "EXIT_SAFELY",
        ]

        self.CHARACTER_TO_NUM: Final[Dict[str, int]] = Setting.list_to_dict(
            self.GRID_CHARACTERS
        )
        self.NUM_TO_CHARACTER: Final[Dict[int, str]] = Setting.swap_dict(
            self.CHARACTER_TO_NUM
        )
        self.OBSERVATION_TO_NUM: Final[Dict[str, int]] = Setting.list_to_dict(
            self.OBSERVATIONS
        )
        self.NUM_TO_OBSERVATION: Final[Dict[int, str]] = Setting.swap_dict(
            self.OBSERVATION_TO_NUM
        )
        self.ACTION_TO_NUM: Final[Dict[str, int]] = Setting.list_to_dict(self.ACTIONS)
        self.NUM_TO_ACTION: Final[Dict[int, str]] = Setting.swap_dict(
            self.ACTION_TO_NUM
        )

        s: dict = Setting.read_settings(stage_name)
        self.PLAYER_MAX_HP: Final[int] = s["PLAYER_MAX_HP"]
        self.ENEMY_POWER: Final[int] = s["ENEMY_POWER"]
        self.PORTION_POWER: Final[int] = s["PORTION_POWER"]
        self.DISTANCE_INF: Final[int] = s["DISTANCE_INF"]
        self.REWARDS: Final[Dict[str, int]] = s["REWARDS"]

    @staticmethod
    def read_settings(stage_name: str) -> dict:
        """
        Read setting corresponding to stage name

        Parameters
        ----------
        stage_name: str

        Returns
        -------
        data: dict

        """
        json_path = path.join("props", f"{stage_name}.json")
        with open(json_path, "r") as f:
            data = json.load(f)
        return data

    @staticmethod
    def list_to_dict(arr: list) -> dict:
        return {arr[i]: i for i in range(len(arr))}

    @staticmethod
    def swap_dict(dic: dict) -> dict:
        return {v: k for k, v in dic.items()}
