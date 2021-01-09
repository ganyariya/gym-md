"""actioner module."""
from typing import List, Tuple

from gym_md.envs.agent.move_info import MoveInfo
from gym_md.envs.setting import Setting

Actions = List[float]


class Actioner:
    """Actioner class.

    アクションの配列を受け取り
    実行するアクションを決定する

    """

    def __init__(self, setting: Setting):
        self.setting: Setting = setting

    def select_action(
        self, actions: Actions, safe_info: MoveInfo, unsafe_info: MoveInfo
    ) -> str:
        """実行するアクションのIDを決定する.

        Parameters
        ----------
        actions: Actions
            エージェントが出力した各アクションの希望値
        safe_info: MoveInfo
            各タイルに移動するための次の座標の辞書
        unsafe_info
            各タイルに移動するための次の座標の辞書
        Returns
        -------
        str
            実行するアクションのID
        """
        actions_idx: List[Tuple[float, int]] = [
            (actions[i], i) for i in range(len(actions))
        ]
        actions_idx.sort(key=lambda z: -z[0])

        for value, idx in actions_idx:
            action_name = self.setting.NUM_TO_ACTION[idx]
            if "SAFELY" in action_name:
                to = safe_info[action_name[0]]
            else:
                to = unsafe_info[action_name[0]]

            # action_nameを実行できない
            if to == (-1, -1):
                continue

            # 実行するアクションのID
            return self.setting.NUM_TO_ACTION[idx]
