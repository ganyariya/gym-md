from typing import Final
import pytest

from gym_md.envs.agent.pather import Pather

Y: Final[int] = 4
X: Final[int] = 0


def test_get_moveinfo(make_pather: Pather):
    move_safe_info = make_pather.get_moveinfo(y=Y, x=X, safe=True)
    move_unsafe_info = make_pather.get_moveinfo(y=Y, x=X, safe=False)

    # safe
    assert move_safe_info['.'] == (3, 0)
    assert move_safe_info['T'] == (3, 0)
    assert move_safe_info['P'] == (-1, -1)

    # unsafe
    assert move_unsafe_info['.'] == (3, 0)
    assert move_unsafe_info['T'] == (3, 0)
    assert move_unsafe_info['E'] == (4, 1)
    assert move_unsafe_info['P'] == (5, 0)


def test_get_distance_and_prev(make_pather: Pather):
    distance_and_prev_safe = make_pather.get_distance_and_prev(y=Y, x=X, safe=True)
    distance_and_prev_unsafe = make_pather.get_distance_and_prev(y=Y, x=X, safe=False)

    distance_safe = distance_and_prev_safe[0]
    prev_safe = distance_and_prev_safe[1]
    assert distance_safe[0][0] == 4
    assert distance_safe[8][0] == make_pather.setting.DISTANCE_INF
    assert distance_safe[6][4] == make_pather.setting.DISTANCE_INF

    assert prev_safe[0][0] == (1, 0)
    assert prev_safe[4][8] == (4, 7)
    assert prev_safe[8][0] == (-1, -1)

    distance_unsafe = distance_and_prev_unsafe[0]
    prev_unsafe = distance_and_prev_unsafe[1]

    assert distance_unsafe[0][0] == 4
    assert distance_unsafe[8][0] == 4
    assert distance_unsafe[6][4] == 10

    assert prev_unsafe[0][0] == (1, 0)
    assert prev_unsafe[4][8] == (4, 7)
    assert prev_unsafe[8][0] == (7, 0)

