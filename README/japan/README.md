# gym-md

`gym-md`は[MiniDungeons](http://minidungeons.com/)と呼ばれるダンジョンゲームを`OpenAI Gym`に移植したものです。
このMiniDungeonsはChristoffer Holmgårdらによって開発されたゲームです。
詳しい説明は[Antonios Liap](http://antoniosliapis.com/projects/project_minidungeons.php)のページにあります。

<p align="center">
    <img src="/README/japan/screen.png" width="200px">
</p>

# How to Install

To use
```bash
pip install gym-md
```

To develop
```bash
git clone  https://github.com/Ganariya/gym-md.git
cd gym-md

# install
pipenv install

# make document
pipenv run build

# test
pipenv run test

# tox (you have to `pipenv install` before tox)
tox
```

# How to Use

```python
import gym
import gym_md
import random

env = gym.make('gym_md:md-test-v0')

LOOP: int = 100
TRY_OUT: int = 100

for _ in range(TRY_OUT):
    observation = env.reset()
    reward_sum = 0
    for i in range(LOOP):
        env.render(mode='human')
        actions = [random.random() for _ in range(7)]
        observation, reward, done, info = env.step(actions)

        reward_sum += reward

        if done:
            env.render()
            break

    print(reward_sum)
```

# Attributes

# Stages
