#!/usr/bin/env python
# encoding: utf-8
#
# See COPYRIGHT and LICENSE files at the top of the source tree.
#

import os
import io

from setuptools import setup, find_packages


PACKAGENAME = 'community_mailbot'
DESCRIPTION = 'Friendly mail forwarding bot for community.lsst.org'
LONG_DESCRIPTION = ''
AUTHOR = 'Jonathan Sick'
AUTHOR_EMAIL = 'jsick@lsst.org'
LICENSE = 'MIT'
URL = 'https://github.com/lsst-sqre/community_mailbot'


def read(filename):
    full_filename = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename)
    with io.open(full_filename, encoding="utf-8") as f:
        return f.read()


setup(
    name=PACKAGENAME,
    # Versions should comply with PEP440.
    # (http://www.python.org/dev/peps/pep-0440)
    version='0.1.2.dev',
    description=DESCRIPTION,
    long_description=read('README.rst'),
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='astronomy discourse email',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['requests', 'mandrill', 'beautifulsoup4'],
    tests_require=[],

    # package_data={},

    entry_points={
        'console_scripts': [
            'forward_discourse=community_mailbot.scripts.forward_discourse:main',  # NOQA
            'discourse_categories=community_mailbot.scripts.discourse_categories:main',  # NOQA
        ],
    },
)
