# gym-md
## 日本語のREADME.md
The original Japanese README can be found [here](https://github.com/ganyariya/gym-md/blob/main/README/japan/README.md).

## Contents
* [Overview](#overview)
* [Installation](#installation)
    + [Installing from PyPI](#installing-from-pypi)
    + [Running build and tests](#running-build-and-tests)
      - [Prerequisites](#prerequisites)
      - [Running the build and tests](#running-the-build-and-tests)
* [Usage](#usage)
* [The MiniDungeons Gym Environment](#the-minidungeons-gym-environment)
    + [Overview](#overview-1)
    + [Actions](#actions)
    + [Environment](#environment)
      - [env object](#env-object)
      - [env.step method](#envstep-method)
* [Levels and Settings](#levels-and-settings)

## Overview
gym-md is a python reimplementation[^1] of the dungeon exploration game [MiniDungeons](http://minidungeons.com/)[^2] created as an [OpenAI Gym](https://gym.openai.com/)[^3] environment. 
MiniDungeons[^2] is a roguelike dungeon exploration game created as a benchmark research domain for modeling decision-making styles of human players[^4]. A Java implementation of MiniDungeons can be found [here](https://github.com/sentientdesigns/minidungeons).

<p align="center">
    <img src="https://github.com/ganyariya/gym-md/blob/main/README/resources/md_stages_screenshots/md-test-v0_step0.jpg?raw=true" width="250px">
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
### Installing from PyPI
The gym-md python package can be found on [pypi](https://pypi.org/project/gym-md/).
To install the latest gym-md package run:
```bash
pip install gym-md
```
### Running build and tests
#### Prerequisites 
The gym-md project makes use of [pipenv](https://pypi.org/project/pipenv/) for the overall project's package management.
In order to build the project's documentation and run the respective tests pipenv will need to be installed.
Please see the 'Installation' section on the [pipenv](https://pypi.org/project/pipenv/) PyPI page.
If you face any issues with the pipenv installation, you can also try installing pipenv using pip (see [source](https://www.codegrepper.com/code-examples/shell/pipenv+not+found+after+pip3+install)).

Furthermore, several additional tests and code linting is orchestrated using [tox](https://tox.wiki/en/latest/),
defined in the [tox.ini](tox.ini) file.
Please see [tox installation](https://tox.wiki/en/latest/install.html#tox-installation) for more detail.

#### Running the build and tests
If you would like to build and install gym-md from source, please run the following commands:
```bash
git clone https://github.com/Ganariya/gym-md.git
cd gym-md

# create the pipenv gym-md build and testing environment
pipenv install

# launch the pipenv environment
pipenv shell

# build gym-md documentation
pipenv run build

# run gym-md tests
pipenv run test

# start the tox testing orchestration
tox

# to build and upload your own gym-md wheel (.whl) file, please see the upload.sh file.
# your custom .whl can be locally installed using: pip install <path to .whl>
rm -f -r gym_md.egg-info/* dist/*
python setup.py bdist_wheel
twine upload dist/*
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
### Overview

<p align="center">
    <img src="https://github.com/ganyariya/gym-md/blob/main/README/resources/gym-md-env-action-loop.drawio.svg?raw=true" width="600px">
</p>

Click [here](https://gym.openai.com/docs/) for a _Getting Started with Gym_ overview.

### Actions
An action within the gym-md environment (_env_) is represented as a python _list_ containing seven (7) floating point values, for example:
```python
actions_eg = [0.7603953105618472,
              0.954037518265538,
              0.7224447519623062,
              0.35121023208759905,
              0.4878166326111911,
              0.6166020008598004,
              0.48734265188517545]
```
Each index in the _actions_ list corresponds to a specific action available for the game agent to take:
- index 0: Head to the monster
- index 1: Head to the treasure
- index 2: Head to the treasure (avoid monsters)
- index 3: Head to the potion
- index 4: Head to the potion (avoid monsters)
- index 5: Head to the exit
- index 6: Head to the exit (avoid monsters)

The environment (_env_) selects the action, within the action float list, which has the highest value.

In the `actions_eg` list example, the action with the highest value is 'Head to the treasure'
(which is index 1, with a value of 0.954037518265538).
However, if the selected highest action is not a valid action within the given state, then the next highest action value is taken.

In the `actions_eg` list example, if the original highest action 'Head to the treasure' (index 1, with a value of 0.954037518265538) cannot be performed (e.g. there is no more treasure to collect) then the next highest action 'Head to the monster'
(which is index 0, with a value of 0.7603953105618472) is chosen. This action selection process is repeated until a valid action can be
performed within the given state. Furthermore, if the desired values are the same, an action is randomly selected.

### Environment
#### env object
The _env_ object created using `env = gym.make('md-test-v0')` is based on the `MdEnvBase` class defined within [md_env.py](gym_md/envs/md_env.py).
The _env_ object contains several objects and methods (only a subset is discussed here, please see [md_env.py](gym_md/envs/md_env.py) for more).
The  _env_ object contains:
- The current stage name
  - `env.stage_name` 
- An internal settings object of the _Setting_ class defined within [setting.py](gym_md/envs/setting.py). This object contains all the stage specific information and configuration. 
  - `env.setting`
    - helpful stage specific info can be accessed within the setting object:
      - `env.setting.PLAYER_MAX_HP`: agent's max hit points.
      - `env.setting.REWARDS`: reward values obtained.
      - `env.setting.ACTIONS`: actions available in the stage.
      - For the full list of setting values please see [setting.py](gym_md/envs/setting.py).

- An internal grid object of the _Grid_ class defined within [grid.py](gym_md/envs/grid.py). This grid object is a grid world representation of the world stage.
  - `env.grid`
    - helpful grid world info can be accessed within the grid object:
      - `env.grid.H`: grid world's height.
      - `env.grid.W`: grid world's width.
      - `env.grid.g`: grid world represented as a 2D list.
      - For the full list of attributes please see [grid.py](gym_md/envs/grid.py).

- An internal agent object of the _Agent_ class defined within [agent.py](gym_md/envs/agent/agent.py). When an action is passed into the env.step method, this internal agent object is used to carry out the action.
  - `env.agent`
    - helpful agent info can be accessed within the agent object:
      - `env.agent.hp`: agent's hit points.
      - `env.agent.y`: agent's y-position in grid world.
      - `env.agent.x`: agent's x-position in grid world.
      - For the full list of attributes please see [agent.py](gym_md/envs/agent/agent.py).

The [OpenAI Gym environment](https://gym.openai.com/docs/) specific methods are discussed as part of the [env.step method](#envstep-method) subsection.

#### env.step method
The gym-md environment's step method returns the following values:
```python
observation, reward, done, info = env.step(actions)
```
- observation (list): the resultant observation of the environment is represented as a list of integers of length eight (8).
  - an example output observation is:
    ```python
    [4, 4, 4, 10, 1000, 8, 8, 30]
    ```
  - each index in the _observation_ list represents the following:
    - index 0: Distance to the monster
    - index 1: Distance to the treasure
    - index 2: Distance to treasure (avoid monsters)
    - index 3: Distance to potion
    - index 4: Distance to potion (avoid monsters)
    - index 5: Distance to the exit
    - index 6: Distance to the exit (avoid monsters)
    - index 7: Agent's physical strength (i.e. _Hit Points (HP)_)
  - some of the observation values received is level specific and can be adjusted/set by modifying the respective level `.json` file, found within the [props](gym_md/envs/props) folder.
    - for example, the 1000 value for index 4 (Distance to potion) corresponds to the "DISTANCE_INF" value set within the [test.json](gym_md/envs/props/test.json) level file.  
- reward (float): amount of reward achieved by the previous action.
  - the reward received is level specific and can be adjusted/set by modifying the respective level `.json` file, found within the [props](gym_md/envs/props) folder.
  - for example, the rewards set in the test level ([test.json](gym_md/envs/props/test.json)) are: 
    ```python
      "REWARDS": {
        "TURN": 1,
        "EXIT": 20,
        "KILL": 4,
        "TREASURE": 3,
        "POTION": 1,
        "DEAD": -20
      }
    ```
- done (boolean): indicated whether the episode has terminated or not. In other words, `True` indicates 'yes, the level has ended', whilst `False` indicates 'no, the level has not yet ended'.
- info (dict): a dictionary containing play data, each action taken by the agent is tracked by this dictionary.
  - an example info output is:
    ```python
    defaultdict(<class 'int'>, {'POTION': 7, '.': 38, 'MONSTER': 9, 'EXIT_SAFELY': 4, 'TREASURE': 3, 'TREASURE_SAFELY': 9, 'EXIT': 6})
    ```
    
## Levels and Settings
New levels can be created by creating your own class which inherits from the [MdEnvBase](gym_md/envs/md_env.py) class. The below example, along with others, can be found within the [md_env_list.py](gym_md/envs/md_env_list.py) script.
```python
from typing import Final

from gym_md.envs.md_env import MdEnvBase

class TestMdEnv(MdEnvBase):
    """TestMdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "test"
        super(TestMdEnv, self).__init__(stage_name=stage_name)
```
You will also need to set the respective level's json file and txt file, found respectively within the [props](gym_md/envs/props) and [stages](gym_md/envs/stages) folders.
Furthermore, you will then need to add the additional levels to the [gym_md.\_\_init\_\_.py](gym_md/__init__.py) and [gym_md.envs.\_\_init\_\_.py](gym_md/envs/__init__.py) files.

For a list of the current available gym_md environment _levels_, please see [Stages README.md](README/resources/md_stages_screenshots/README.md). For a simpler level list view please see [env_levels.txt](README/resources/env_levels.txt).
Both the _Stages README.md_ and _env_levels.txt_ files contains the env levels registered within the [gym_md.\_\_init\_\_.py](gym_md/__init__.py).
