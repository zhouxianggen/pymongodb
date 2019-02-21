#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pymongodb',
        version = '1.0',
        install_requires = ['pymongo'], 
        description = 'python mongodb api',
        url = 'https://github.com/zhouxianggen/pymongodb', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pymongodb'],
        data_files = [ ],  
        entry_points = { }   
        )
