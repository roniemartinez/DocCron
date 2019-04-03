#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import time

import doccron


def foo():
    """
    /etc/crontab::

        * * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "foo")


def bar():
    """
    /etc/crontab::

        * * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "bar")


if __name__ == '__main__':
    doccron.run_jobs()
