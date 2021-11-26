from random import Random
from gym_md.envs.md_env import MdEnvBase


def test_is_same_random(make_gym: MdEnvBase):
    make_gym.set_random_seed(20)
    assert id(make_gym.random) == id(make_gym.agent.random)
    assert id(make_gym.random) == id(make_gym.agent.actioner.random)
    arr1 = [make_gym.random.random() for _ in range(10)]

    make_gym.set_random_seed(20)  # リセットされる
    assert id(make_gym.random) == id(make_gym.agent.random)
    assert id(make_gym.random) == id(make_gym.agent.actioner.random)
    arr2 = [make_gym.random.random() for _ in range(10)]
    assert arr1 == arr2

    make_gym.random = Random()  # 入れ直すとだめ
    assert id(make_gym.random) != id(make_gym.agent.random)
    assert id(make_gym.random) != id(make_gym.agent.actioner.random)
