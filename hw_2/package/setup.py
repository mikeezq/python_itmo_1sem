from setuptools import setup, find_packages

import json
import os

def read_pipenv_dependencies(fname):
    """Получаем из Pipfile.lock зависимости по умолчанию."""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]

if __name__ == '__main__':
    setup(
        name='latex_functions',
        version=os.getenv('PACKAGE_VERSION', '0.0.1'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'latex_functions*'
        ]),
        description='A package for some latex functions.',
        install_requires=[
              *read_pipenv_dependencies('Pipfile.lock'),
        ]
    )