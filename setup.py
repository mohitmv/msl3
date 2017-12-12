
from setuptools import setup


import msl

setup(
	name='msl',
	version=msl.msl['__version__'],
	url='https://github.com/mohitmv/msl3',
	author='Mohit Saini',
	author_email='mohitsaini1196@gmail.com',
	description='Simple extension of python inbuilt functions',
	long_description='Simple extension of python inbuilt functions',
	packages=["msl", "msl.utils"],
	install_requires=[],
	extras_require={}, 
	classifiers=[
		'Programming Language :: Python :: 3',
	],
	entry_points={}
)

