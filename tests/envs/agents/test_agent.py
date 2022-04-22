import copy
from random import Random

from gym_md.envs.agent.agent import Agent

NAME: str = 'test'


def test_select_action(make_agent: Agent):
    exit_safely_actions = [0, 4, 2, 3, -5, 1, 8]
    exit_safely = make_agent.select_action(exit_safely_actions)
    assert exit_safely == "EXIT_SAFELY"

    monster_actions = [-1, -2, -2, -2, -2, -2, -2]
    monster_safely = make_agent.select_action(monster_actions)
    assert monster_safely == "MONSTER"

    treasure_safely_actions = [0, 0, 2, 0, 0, 0, 1]
    treasure_safely = make_agent.select_action(treasure_safely_actions)
    assert treasure_safely == "TREASURE_SAFELY"

    potion_safely_actions = [0, 0, 0, 0, 4, 0, 1]
    potion_safely_but_monster = make_agent.select_action(potion_safely_actions)
    assert potion_safely_but_monster == "EXIT_SAFELY"


def test_agent_attacked_by_enemy_random(make_agent: Agent) -> None:
    attacked_hitpoints = []
    default_hp = -1

    for _ in range(1000):
        agent = copy.deepcopy(make_agent) # 体力 40
        agent.random = Random() # seed 値が同じだと同じ攻撃力になる
        default_hp = agent.hp # 40 をデフォルトに入れる
        agent.be_influenced(8, 0) # 戦わせる
        attacked_hitpoints.append(agent.hp)

    exist_random = False
    for x in attacked_hitpoints:
        if x % 10 != 0:
            exist_random = True
    assert exist_random
    assert default_hp - make_agent.setting.ENEMY_POWER_MIN == max(attacked_hitpoints)
    assert default_hp - make_agent.setting.ENEMY_POWER_MAX == min(attacked_hitpoints)


def test_agent_attacked_not_random(make_agent: Agent) -> None:
    attacked_hitpoints = []
    for _ in range(100):
        agent = copy.deepcopy(make_agent)
        agent.random = Random() # seed 値が同じだと同じ攻撃力になる
        # ランダム攻撃をやめる
        agent.setting.IS_ENEMY_POWER_RANDOM = False
        agent.be_influenced(8, 0)
        attacked_hitpoints.append(agent.hp)

    exist_random = False
    for x in attacked_hitpoints:
        if x % 10 != 0:
            exist_random = True
    assert not exist_random


def test_agent_hp_not_max_limit(make_agent: Agent) -> None:
    # 制限しない
    make_agent.setting.IS_PLAYER_HP_LIMIT = False
    for _ in range(100):
        make_agent.be_influenced(6, 4)
    assert make_agent.hp >= 1000


def test_agent_hp_max_limit(make_agent: Agent) -> None:
    # 制限する
    make_agent.setting.IS_PLAYER_HP_LIMIT = True
    for _ in range(100):
        make_agent.be_influenced(6, 4)
    assert make_agent.hp == make_agent.setting.PLAYER_MAX_HP


def test_agent_previous_hp(make_agent: Agent) -> None:
    assert make_agent.hp == 30
    previous_hp = 20
    make_agent.change_player_hp(previous_hp)
    assert make_agent.hp == previous_hp

    make_agent.be_influenced(8, 0)
    assert make_agent.hp < previous_hp

    make_agent.change_player_hp(30)
    assert make_agent.hp == 30

    over_hp = 50
    make_agent.change_player_hp(over_hp)
    assert make_agent.hp == 30
