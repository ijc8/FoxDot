#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as f:
    long_description=f.read()

with open("FoxDotPatterns/lib/.version", "r") as f:
    version = f.read()

setup(
    name='FoxDotPatterns',
    version=version,
    description='Small subset of the FoxDot livecoding environment.',
    author='Ryan Kirkbride',
    author_email='ryan@foxdot.org',
    license='cc-by-sa-4.0',
    url='http://foxdot.org/',
    packages=['FoxDotPatterns',
            'FoxDotPatterns.lib',
            'FoxDotPatterns.lib.Patterns',
            'FoxDotPatterns.lib.Utils'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data = {'FoxDotPatterns': [
        'snd/*/*',
        'snd/*/*/*',
        'lib/.version',
        'README.md',
    ]}
)


