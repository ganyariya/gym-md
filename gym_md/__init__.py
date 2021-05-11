"""gym-md init module."""
__version__ = "0.4.2"

from logging import NullHandler, getLogger

from gym.envs.registration import register

getLogger(__name__).addHandler(NullHandler())

register(
    id="md-base-v0",
    entry_point="gym_md.envs:MdEnvBase",
)
register(
    id="md-test-v0",
    entry_point="gym_md.envs:TestMdEnv",
)
register(
    id="md-edge-v0",
    entry_point="gym_md.envs:EdgeMdEnv",
)
register(
    id="md-hard-v0",
    entry_point="gym_md.envs:HardMdEnv",
)
register(
    id="md-random_1-v0",
    entry_point="gym_md.envs:Random1MdEnv",
)
register(
    id="md-random_2-v0",
    entry_point="gym_md.envs:Random2MdEnv",
)
for i in range(2):
    register(
        id=f"md-gene_{i + 1}-v0",
        entry_point=f"gym_md.envs:Gene{i + 1}MdEnv",
    )
for i in range(5):
    register(
        id=f"md-strand_{i + 1}-v0",
        entry_point=f"gym_md.envs:Strand{i + 1}MdEnv",
    )
for i in range(3):
    register(
        id=f"md-check_{i + 1}-v0",
        entry_point=f"gym_md.envs:Check{i + 1}MdEnv",
    )
