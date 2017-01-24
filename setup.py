from setuptools import find_packages
from setuptools import setup


setup(
    name='dumb-pypi',
    version='0.0.0',
    author='Chris Kuehl',
    author_email='ckuehl@ocf.berkeley.edu',
    py_modules=('dumb_pypi',),
    classifiers={
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    },
    entry_points={
        'console_scripts': (
	    'dumb-pypi = dumb_pypi.main',
        ),
    },
)