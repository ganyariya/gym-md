from gym_md.envs.md_env import MdEnvBase


def test_gym_run(make_gym: MdEnvBase) -> None:
    state = make_gym.reset()
    for _ in range(10):
        make_gym.step(make_gym.action_space.sample())


def test_gym_previous_hp(make_gym: MdEnvBase) -> None:
    assert make_gym.agent.hp == 30
    previous_hp = 10
    make_gym.change_player_hp(previous_hp)
    assert make_gym.agent.hp == previous_hp

    previous_hp = 100
    make_gym.change_player_hp(previous_hp)
    assert make_gym.agent.hp == make_gym.setting.PLAYER_MAX_HP