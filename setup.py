from setuptools import setup, find_packages
import os

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath: str) -> list:
    """
    Read dependencies from requirements.txt
    """
    with open(filepath, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='Rakshit',
    author_email='rakshitchopra788@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirmenst.txt')
)
