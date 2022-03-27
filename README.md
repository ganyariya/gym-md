# gym-md

## 日本語のREADME.md
The original Japanese README can be found [here](README/japan/README.md).

## Overview
gym-md is a python reimplementation[^1] of the dungeon exploration game [MiniDungeons](http://minidungeons.com/)[^2] created as an [OpenAI Gym](https://gym.openai.com/)[^3] environment. 
MiniDungeons[^2] is a roguelike dungeon exploration game created as a benchmark research domain for modeling decision-making styles of human players[^4]. A Java implementation of MiniDungeons can be found [here](https://github.com/sentientdesigns/minidungeons).

<p align="center">
    <img src="/README/resources/screen.png" width="250px">
</p>

[^1]: Y. Iwasaki. and K. Hasebe., “A framework for generating playstyles
of game ai with clustering of play logs,” in Proceedings of the 14th
International Conference on Agents and Artificial Intelligence - Volume
3: ICAART,, INSTICC. SciTePress, 2022, pp. 605–612.
[^2]: C. Holmgård, A. Liapis, J. Togelius, and G. N. Yannakakis, “Evolving
personas for player decision modeling,” in 2014 IEEE Conference on
Computational Intelligence and Games, 2014, pp. 1–8.
[^3]: G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, and W. Zaremba, “Openai gym,” arXiv preprint
arXiv:1606.01540, 2016.
[^4]: A. Liapis, “Minidungeons”, website, 2022. Accessed on: Mar. 27, 2022. [Online].
Available: http://antoniosliapis.com/projects/project_minidungeons.php

## Installation
The gym-md python package can be found on pypi at https://pypi.org/project/gym-md/.
To install the latest gym-md package run:
```bash
pip install gym-md
```
If you would like to build and install gym-md from source, please run the following commands:
```bash
git clone https://github.com/Ganariya/gym-md.git
cd gym-md

# install
pipenv install

# make document
pipenv run build

# test
pipenv run test

# tox (you have to `pipenv install` beforehand)
tox
```

## Usage
```python
import gym
import gym_md
import random

env = gym.make('md-test-v0')

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

## The MiniDungeons Gym Environment
Click [here](https://gym.openai.com/docs/) for a _Getting Started with Gym_ overview.

### Actions
An action within the gym-md environment (_env_) is represented as a python _list_ containing seven floating point values, for example:
```python
[0.7603953105618472,
 0.954037518265538,
 0.7224447519623062,
 0.35121023208759905,
 0.4878166326111911,
 0.6166020008598004,
 0.48734265188517545]
```
Each element in the array corresponds to a specfic action available for the game agent to take.

### Environment
The gym-md environment's step method returns the following values:
