from setuptools import setup, find_packages
import os

version = '1.2.2.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'dynatree', 'test_dynatree.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.dynatree',
    version=version,
    description="fanstatic dyntree jQuery.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Lugensa GmbH',
    author_email='jd@lugensa.com',
    url='https://github.com/lugensa/js.dynatree',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.jquery',
        'js.jqueryui',
        ],
    entry_points={
        'fanstatic.libraries': [
            'js.dynatree = js.dynatree:library',
            ],
        },
    )
