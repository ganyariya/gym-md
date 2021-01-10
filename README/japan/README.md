# gym-md

`gym-md`は[MiniDungeons](http://minidungeons.com/)と呼ばれるダンジョンゲームを`OpenAI Gym`に移植したものです。  
このMiniDungeonsはChristoffer Holmgårdらによって開発されたゲームです。  
詳しい説明は[Antonios Liap](http://antoniosliapis.com/projects/project_minidungeons.php)のページにあります。  

<p align="center">
    <img src="/README/resources/screen.png" width="200px">
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

# tox (you have to `pipenv install` beforehand)
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

# Schemes

エージェントは`env`環境から状態として、長さが8のintの配列を受け取ります。
それぞれ以下を表しています。  

- エージェントの体力
- モンスターまでの距離
- 宝物までの距離
- 宝物までの距離（モンスターを避ける）
- ポーションまでの距離
- ポーションまでの距離（モンスターを避ける）
- 出口までの距離
- 出口までの距離（モンスターを避ける）

エージェントは`env`環境に行動として、長さが7のfloatの配列を出力します。  
それぞれ以下を表しています。  
env環境は、このうち最大の値を持つエージェントの行動を選択します。  
しかし、その行動がステージの状態を考慮すると動作できない場合は、次に大きい値の行動を選択することを繰り返します。

たとえば、もし`宝物に向かう`が最大だったとしてもステージに宝物がなければ向かうことができません。よって、その場合は次に大きい値の行動を環境が自動で選択します。

- モンスターに向かう
- 宝物に向かう
- 宝物に向かう（モンスターを避ける）
- ポーションに向かう
- ポーションに向かう（モンスターを避ける）
- 出口に向かう
- 出口に向かう（モンスターを避ける）

<p align="center">
    <img src="/README/resources/schema.png" width="200px">
</p>

# ステージと設定

ステージは`MdEnvBase`クラスを継承したクラスを作成することで作ることができます。  
具体的には、ソースコードの`TestMdEnv`クラスを参照ください。  
また、設定したステージの名前に対応した`jsonファイル`ならびに`txtファイル`を設定する必要があります。  
`test.json`, `test.txt`ファイルを参考にしてください。
また、その後`gym_md.__init__.py`と`gym_md.envs.__init__.py`に追加ステージの設定を行う必要があります。  

## リスト

以下はすでに設定されているステージです。
設定については各ステージの`stage_name.json`をご確認ください。

|名前|イメージ|
|:-:|:-:|
|Test|![](/README/resources/screen.png)|

