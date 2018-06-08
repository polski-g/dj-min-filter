import os
import re
from codecs import open
from setuptools import setup, find_packages


def get_version(*file_paths):
    """Retrieves the version from min_filter/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

version = get_version("min_filter", "__init__.py")
install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='min_filter',
    version=version,
    description='Template filter to insert .min just before .js/.css when in DEBUG mode',
    long_description=readme,
    author='polski-g',
    author_email='polski_g@sent.at',
    url='https://github.com/polski-g/dj-min-filter',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=install_requires,
    license="LGPL",
    classifiers=[
        'Intended Audience :: Developers',
        'Framework :: Django :: 1.11',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
    keywords='dj-min-filter',
)
