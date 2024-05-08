#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='promtimer',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'promtimer = promtimer.promtimer:main',
        ],
    }
)
