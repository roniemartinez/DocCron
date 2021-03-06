#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import time


def hello():
    """
    Print "hello world" every 2nd second and 3rd second:

    /etc/crontab::

        */2 * * * * *
        */3 * * * * *
    """
    print(time.strftime("%Y-%m-%d %H:%M:%S"), "hello world")


if __name__ == "__main__":
    import doccron

    doccron.run_jobs(quartz=True)
