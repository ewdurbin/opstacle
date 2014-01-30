#!/usr/bin/env python

from setuptools import setup

import os
import re

base_path = os.path.dirname(__file__)

fp = open(os.path.join(base_path, 'opstacle', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(fp.read()).group(1)
fp.close()

version = VERSION

def read(fname):
    try:
        path = os.path.join(os.path.dirname(__file__), fname)
        return open(path).read()
    except IOError:
        return ""

requirements =      ['inbox<0.0.6']

setup(
    name='opstacle',
    version=version,
    license='MIT',
    description="A dangerous and probably broken SMTP proxy that attempts to keep you sane",
    long_description=read('README.rst'),
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: System :: Networking :: Monitoring'
    ],
    keywords='',
    author='Ernest W. Durbin III',
    author_email='ewdurbin@gmail.com',
    url='https://github.com/ewdurbin/opstacle/',
    packages=['opstacle'],
    scripts=['bin/opstacle'],
    install_requires=requirements
)
