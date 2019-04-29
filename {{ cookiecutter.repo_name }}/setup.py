from setuptools import find_packages, setup
import subprocess

# Get current version number from git'
__version__ = subprocess.check_output(['git', 'describe', '--abbrev=0']).strip()
__version__ = str(__version__)[2:-1]

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL-3.0{% endif %}',
    setup_requires=['pytest-runner'],
    tests_requires=['pytest', 'pytest-mypy', 'pytest-instafail']
)
