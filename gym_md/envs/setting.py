"""setting module.

設定のモジュール．
ステージ名を受け取り，そのステージ名にあったステージ読み込みと定数読み込みを行う．

"""
import json
from copy import deepcopy
from os import path
from typing import Dict, Final, List

from gym_md.envs import definition
from gym_md.envs.singleton import Singleton
from gym_md.envs.config.props_config import PropsConfig, RewardsConfig


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
        self.GRID_CHARACTERS: Final[List[str]] = definition.GRID_CHARACTERS
        self.OBSERVATIONS: Final[List[str]] = definition.OBSERVATIONS
        self.ACTIONS: Final[List[str]] = definition.ACTIONS
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

        props_config = Setting.read_settings(stage_name)
        self.PLAYER_MAX_HP: Final[int] = props_config.PLAYER_MAX_HP
        self.ENEMY_POWER: Final[int] = props_config.ENEMY_POWER
        self.PORTION_POWER: Final[int] = props_config.PORTION_POWER
        self.DISTANCE_INF: Final[int] = props_config.DISTANCE_INF
        self.RENDER_WAIT_TIME: Final[float] = props_config.RENDER_WAIT_TIME
        self.REWARDS: RewardsConfig = deepcopy(props_config.REWARDS)
        self.ORIGINAL_REWARDS: RewardsConfig = deepcopy(props_config.REWARDS)

    def change_reward_values(self, rewards: Dict[str, int]) -> None:
        """報酬を変更する.

        Parameters
        ----------
        rewards: dict of (str, int)
        """
        for key, value in rewards.items():
            setattr(self.REWARDS, key, value)

    def restore_reward_values(self):
        for key, value in self.ORIGINAL_REWARDS.dict().items():
            setattr(self.REWARDS, key, value)

    @staticmethod
    def read_settings(stage_name: str) -> PropsConfig:
        """Read setting corresponding to stage name.

        ステージ名にあった設定を読み込む
        Pydantic で読み込む

        Parameters
        ----------
        stage_name: str

        Returns
        -------
        PropsConfig

        """
        file_dir = path.dirname(__file__)
        json_path = path.join(file_dir, "props", f"{stage_name}.json")
        with open(json_path, "r") as f:
            data = json.load(f)
            props_config = PropsConfig(**data)
        return props_config

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
