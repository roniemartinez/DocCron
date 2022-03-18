
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='doccron',
    version='1.6.1',
    description='Schedule with Docstrings',
    python_requires='==3.*,>=3.7.0',
    project_urls={"repository": "https://github.com/roniemartinez/DocCron"},
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    license='MIT',
    keywords='crontab cron docstring',
    classifiers=['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10', 'Programming Language :: Python :: Implementation :: CPython'],
    packages=['DocCron'],
    package_dir={"": "."},
    package_data={},
    install_requires=['python-dateutil==2.*,>=2.8.1'],
    extras_require={"dev": ["autoflake==1.*,>=1.3.1", "black==22.*,>=22.1.0", "codecov==2.*,>=2.0.16", "dephell==0.*,>=0.8.3", "flake8==4.*,>=4.0.1", "freezegun==1.*,>=1.2.0", "isort==5.*,>=5.10.1", "mypy==0.*,>=0.941.0", "pyproject-flake8==0.*,>=0.0.1.a2", "pytest==7.*,>=7.0.1", "pytest-cov==3.*,>=3.0.0", "tomlkit==0.7.0", "types-freezegun==1.*,>=1.1.7", "types-python-dateutil==2.*,>=2.8.10"]},
)
