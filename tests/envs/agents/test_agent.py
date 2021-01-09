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

    portion_safely_actions = [0, 0, 0, 0, 4, 0, 1]
    portion_safely_but_monster = make_agent.select_action(portion_safely_actions)
    assert portion_safely_but_monster == "EXIT_SAFELY"
