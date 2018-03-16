#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup, find_packages

SCRIPT_DIR = path.dirname(path.realpath(__file__))
VERSION_PATH = path.join(SCRIPT_DIR, 'keep-current', 'version.py')

with open(VERSION_PATH, 'r') as version_file:
    exec(version_file.read())
VERSION = __version__  # @UndefinedVariable

LONG_DESCRIPTION = ' After studying a topic, keeping current with the news, ' \
                   ' published papers, advanced technologies and such ' \
                   ' proved to be a hard work.' \
                   ' This automated tool aspire to make this process easier'
KEYWORDS = 'neural network language modeling machine learning research'
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Environment :: Console',
               'Programming Language :: Python :: 3',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: Apache Software License',
               'Operating System :: OS Independent',
               'Topic :: Scientific/Engineering']

setup(name='KeepCurrent',
      version=VERSION,
      author='Liad Magen',
      author_email='liad.magen@gmail.com',
      url="https://github.com/liadmagen/Keep-Current",
      description='Stay current with your profession',
      long_description=LONG_DESCRIPTION,
      license='Apache License, Version 2.0',
      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,
      packages=find_packages(exclude=['tests']),
      package_data={'keepCurrent': ['architectures/*.arch']},
      scripts=[],
      install_requires=[
          'numpy',
          'tox',
          'logzero',
          'beautifulsoup4',
          'scrapy',
          'nltk',
          'gensim',
          'spacy',
          'textblob',
          'tensorflow',
          'keras',
          'tornado',
          'pymongo',
          'Flask',
          'connexion',
          'Flask-Injector',
          'fastavro',
          'nose',
          'sphinx'
      ],
      test_suite='tests')
