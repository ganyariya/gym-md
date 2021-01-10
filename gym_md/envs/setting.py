"""setting module.

設定のモジュール．
ステージ名を受け取り，そのステージ名にあったステージ読み込みと定数読み込みを行う．

"""
import json
from os import path
from typing import Dict, Final, List

from gym_md.envs.singleton import Singleton


class Setting(Singleton):
    """ステージに関する設定ファイル.

    シングルトンで設計されている．

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
        self.RENDER_WAIT_TIME: Final[int] = s["RENDER_WAIT_TIME"]
        self.REWARDS: Final[Dict[str, int]] = s["REWARDS"]

    @staticmethod
    def read_settings(stage_name: str) -> dict:
        """Read setting corresponding to stage name.

        ステージ名にあった設定を読み込む

        Parameters
        ----------
        stage_name: str

        Returns
        -------
        dict

        """
        file_dir = path.dirname(__file__)
        json_path = path.join(file_dir, "props", f"{stage_name}.json")
        with open(json_path, "r") as f:
            data = json.load(f)
        return data

    @staticmethod
    def list_to_dict(arr: list) -> dict:
        """リストを辞書にインデックス付きで変換する.

        Parameters
        ----------
        arr: list

        Returns
        -------
        dict

        """
        return {arr[i]: i for i in range(len(arr))}

    @staticmethod
    def swap_dict(dic: dict) -> dict:
        """辞書のkey, valueを入れ替えた辞書を作る.

        Parameters
        ----------
        dic: dict

        Returns
        -------
        dict

        """
        return {v: k for k, v in dic.items()}
