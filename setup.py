#!/usr/bin/env python
# encoding: utf-8
#
# See COPYRIGHT and LICENSE files at the top of the source tree.
#

from setuptools import setup, find_packages
import os


PACKAGENAME = 'community_mailbot'
DESCRIPTION = 'Friendly mail forwarding bot for community.lsst.org'
LONG_DESCRIPTION = ''
AUTHOR = 'Jonathan Sick'
AUTHOR_EMAIL = 'jsick@lsst.org'
LICENSE = 'GPLv3'
URL = 'https://github.com/lsst-sqre/community_mailbot'


def read(filename):
    full_filename = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename)
    return open(full_filename).read()

long_description = read('README.rst')


setup(
    name=PACKAGENAME,
    # Versions should comply with PEP440.
    # (http://www.python.org/dev/peps/pep-0440)
    version='0.1.0.dev',
    description=DESCRIPTION,
    long_description=long_description,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='astronomy discourse email',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['requests'],
    tests_require=['pytest',
                   'pytest-pep8',
                   'pytest-cov'],

    # package_data={},

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
