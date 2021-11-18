import gym
import gym_md

from gym_md.envs.md_env import MdEnvBase


def test_read_holmgard_gym() -> None:
    for i in range(11):
        env: MdEnvBase = gym.make(f'md-holmgard_{i}-v0')
        env.reset()
        for j in range(10):
            # if j <= 10:
            #     env.render()
            env.step(env.action_space.sample())


def test_read_constant_holmgard_gym() -> None:
    for i in range(11):
        env: MdEnvBase = gym.make(f'md-constant-holmgard_{i}-v0')
        env.reset()
        for j in range(10):
            # if j <= 10:
            #     env.render()
            env.step(env.action_space.sample())
            assert abs(env.agent.hp) % 10 == 0
