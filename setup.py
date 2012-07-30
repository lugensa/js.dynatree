from setuptools import setup, find_packages
import os

version = '1.0.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'dyntree', 'test_dytree.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.dyntree',
    version=version,
    description="fanstatic dyntree jQuery.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Lugensa GmbH',
    author_email='jd@lugensa.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'dyntree = js.dyntree:library',
            ],
        },
    )
