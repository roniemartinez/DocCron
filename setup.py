from setuptools import setup

VERSION = '1.2.2'

setup(
    name='DocCron',
    version=VERSION,
    packages=['doccron'],
    url='https://github.com/roniemartinez/DocCron',
    download_url='https://github.com/roniemartinez/DocCron/tarball/{}'.format(VERSION),
    license='MIT',
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    description='Schedule with Docstrings',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: Implementation :: CPython']
)
