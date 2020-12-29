from setuptools import setup, find_packages
from glob import glob

setup(
    name='gym_md',
    version='0.0.4',
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
    package_data={
        # 'gym_md': ['gym_md/envs/tiles/*.png']
    },
    data_files=[
        # ('bitfiles', glob('gym_md/envs/tiles/*'))
    ],
    include_package_data=True,
    install_requires=['gym']
)
