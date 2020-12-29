from setuptools import setup, find_packages
from glob import glob

setup(
    name='gym_md',
    version='0.0.3',
    description='OpenAI Gym Environment for MiniDungeons',
    url='https://github.com/Ganariya/gym-md',
    author='ganariya',
    author_email='ganariya2525@gmail.com',
    license='MIT',
    # packages=find_packages(where='gym_md'),
    packages=[
        'gym_md',
        'gym_md.envs',
    ],
    data_files=[
        # ('bitfiles', glob('gym_md/envs/tiles/*'))
    ],
    install_requires=['gym']
)
