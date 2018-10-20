#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
import logging
import sys
import time

import doccron

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s')


def foo():
    """
    * * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "foo")


def bar():
    """
    * * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "bar")


if __name__ == '__main__':
    doccron.run_jobs()
