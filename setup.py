#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	entry_points={
		'console_scripts' : [
			'sleepdungeon=sleepdungeon:run'
		]
	}
)
