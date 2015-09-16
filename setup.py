#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'argparse',
    'click==5.1',
    'colorama==0.3.3',
]

# installs backport_collections on py26
try:
    from collections import Counter
except ImportError:
    requirements.append('backport_collections==0.1')


test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='fosscon2015',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="CLI examples",
    long_description=readme + '\n\n' + history,
    author="Dave Forgac",
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/fosscon2015',
    packages=[
        'fosscon2015',
    ],
    package_dir={'fosscon2015':
                 'fosscon2015'},
    entry_points={
        'console_scripts':[
            'fosscon-argparse=fosscon2015.cli_argparse:cli',
            'fosscon-click=fosscon2015.cli_click:cli',
            'hello-argparse=fosscon2015.hello_argparse:hello',
            'hello-click=fosscon2015.hello_click:hello',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='fosscon2015',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
