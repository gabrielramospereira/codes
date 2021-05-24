#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name = 'FruitBasket',
    version = '1.0',
    license = "",
    author='DanielNReboucas',
    author_email='danielnreboucas@hotmail.com',
    url = "",
    description='Fruit Basket',
    zip_safe=False,
    packages=find_packages(),
    package_data = { 'fruitbasket': [
        '*',
        'htdocs/js/*.js',
        'htdocs/css/*.css',
        'templates/*.html'
    ] },
    entry_points = {
        'trac.plugins': [
            'fruitbasket = fruitbasket.web_ui',
        ],
    },
)