from setuptools import setup, find_packages

setup(
    name='game',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['start_game = game.game:kirill_polniy_dibil']
    },
    install_requires=[
        'pygame==1.9.6'
    ],
)