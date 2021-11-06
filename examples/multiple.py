import time

import doccron


def foo() -> None:
    """
    /etc/crontab::

        * * * * *
    """
    print(time.strftime("%Y-%m-%d %H:%M:%S"), "foo")


def bar() -> None:
    """
    /etc/crontab::

        * * * * *
    """
    print(time.strftime("%Y-%m-%d %H:%M:%S"), "bar")


if __name__ == "__main__":
    doccron.run_jobs()
