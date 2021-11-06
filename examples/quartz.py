import time


def hello() -> None:
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
