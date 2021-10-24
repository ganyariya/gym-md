from gym_md.envs.md_env import MdEnvBase

def test_gym_run(make_gym: MdEnvBase) -> None:
    state = make_gym.reset()
    for _ in range(10):
        make_gym.step(make_gym.action_space.sample())
