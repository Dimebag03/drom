"""Setup File"""

from setuptools import setup


setup(
    name='drom',
    version='0.0.1',
    packages=['drom'],
    entry_points={
        'console_scripts': [
            'drom = drom.drom:main'
        ]
    },
    description="Find the ROM you want to play and make the download from the terminal!",
    license="MIT"
)
