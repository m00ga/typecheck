#!/usr/bin/python3
from setuptools import setup
import config

setup(
    name='typecheck-m00ga',
    version=config.__version__,
    packages=['typecheck'],
    author=config.__author__,
    description='Useful module for runtime type checking',
    setup_requires=['wheel']
)
