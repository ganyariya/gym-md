"""gym-md init module."""
__version__ = "0.2.4"

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
