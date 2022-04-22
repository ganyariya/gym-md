"""setting module.

設定のモジュール．
ステージ名を受け取り，そのステージ名にあったステージ読み込みと定数読み込みを行う．

"""
import json
from copy import deepcopy
from os import path, listdir
from typing import Dict, Final, List
from platform import system as platform_system

from gym_md.envs import definition
from gym_md.envs.config.props_config import PropsConfig, RewardsConfig
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
        self.IS_PLAYER_HP_LIMIT = props_config.IS_PLAYER_HP_LIMIT
        self.ENEMY_POWER = props_config.ENEMY_POWER
        self.ENEMY_POWER_MIN = props_config.ENEMY_POWER_MIN
        self.ENEMY_POWER_MAX = props_config.ENEMY_POWER_MAX
        self.IS_ENEMY_POWER_RANDOM = props_config.IS_ENEMY_POWER_RANDOM
        self.POTION_POWER = props_config.POTION_POWER
        self.DISTANCE_INF = props_config.DISTANCE_INF
        self.RENDER_WAIT_TIME = props_config.RENDER_WAIT_TIME
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
        file_dir: str = path.dirname(__file__)
        target_stage_file: str = f"{stage_name}.json"
        json_path: str = path.join(file_dir, "props", target_stage_file)

        if platform_system().lower() == "linux":
            prop_files_dir: list = listdir(path.join(file_dir, "props"))
            prop_files_dir_lowercased: list = [file_name.lower() for file_name in prop_files_dir]
            actual_stage_file: str = prop_files_dir[prop_files_dir_lowercased.index(target_stage_file.lower())]
            json_path: str = path.join(file_dir, "props", actual_stage_file)

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
