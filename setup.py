"""Setup File"""

from setuptools import setup, find_packages


setup(
    name='drom',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['docutils>=0.3'],
    scripts=['drom.py'],
    entry_points={
        'console_scripts': [
            'drom = drom:main'
        ]
    },
    description="Find the ROM you want to play and make the download from the terminal!",
    license="MIT"
)
