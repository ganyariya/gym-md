"""gym-md init module."""
__version__ = "0.1.1"

from gym.envs.registration import register

register(
    id="md-v0",
    entry_point="gym_md.envs:MdEnv",
)
