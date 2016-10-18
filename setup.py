try:
    import setuptools
except ImportError:
    pass

from setuptools import setup

setup(name='infinite-HALE',
	version='1.0',
	description='Tools for Generating and Simulating Cellular Solids',
	author='Daniel Cellucci & Nick Cramer',
	url='https://github.com/cram9030/infinite-HALE.git',
	packages=[''],
	install_requires=[
		'numpy',
		'scipy',
		'networkx',
		'matplotlib',
		'cvxopt',
	]
	)
