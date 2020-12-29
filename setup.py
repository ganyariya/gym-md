from setuptools import setup, find_packages

setup(
    name='gym_md',
    version='0.0.2',
    description='OpenAI Gym Environment for MiniDungeons',
    url='https://github.com/Ganariya/gym-md',
    author='ganariya',
    author_email='ganariya2525@gmail.com',
    license='MIT',
    # packages=find_packages(where='gym_md'),
    packages=[
        'gym_md',
        'gym_md.envs'
    ],
    install_requires=['gym']
)
