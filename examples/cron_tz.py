import time


def hello() -> None:
    """
    Print "hello world" at every 2nd minute and 3rd minute:

    /etc/crontab::

        CRON_TZ=UTC
        */2 * * * *
        */3 * * * *
    """
    print(time.strftime("%Y-%m-%d %H:%M:%S%z"), "hello world")


if __name__ == "__main__":
    import doccron

    doccron.run_jobs()
