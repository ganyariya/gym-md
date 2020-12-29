import gym


class MdEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def reset(self):
        pass

    def step(self, action):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
