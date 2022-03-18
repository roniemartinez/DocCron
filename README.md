<table>
    <tr>
        <td>License</td>
        <td><img src='https://img.shields.io/pypi/l/DocCron.svg?style=for-the-badge' alt="License"></td>
        <td>Version</td>
        <td><img src='https://img.shields.io/pypi/v/DocCron.svg?logo=pypi&style=for-the-badge' alt="Version"></td>
    </tr>
    <tr>
        <td>Github Actions</td>
        <td><img src='https://img.shields.io/github/workflow/status/roniemartinez/DocCron/Python?label=actions&logo=github%20actions&style=for-the-badge' alt="Github Actions"></td>
        <td>Coverage</td>
        <td><img src='https://img.shields.io/codecov/c/github/roniemartinez/DocCron/branch?label=codecov&logo=codecov&style=for-the-badge' alt="CodeCov"></td>
    </tr>
    <tr>
        <td>Supported versions</td>
        <td><img src='https://img.shields.io/pypi/pyversions/DocCron.svg?logo=python&style=for-the-badge' alt="Python Versions"></td>
        <td>Wheel</td>
        <td><img src='https://img.shields.io/pypi/wheel/DocCron.svg?style=for-the-badge' alt="Wheel"></td>
    </tr>
    <tr>
        <td>Status</td>
        <td><img src='https://img.shields.io/pypi/status/DocCron.svg?style=for-the-badge' alt="Status"></td>
        <td>Downloads</td>
        <td><img src='https://img.shields.io/pypi/dm/DocCron.svg?style=for-the-badge' alt="Downloads"></td>
    </tr>
</table>

# DocCron

Schedule with Docstrings

## Installation

```bash
pip install DocCron
```

## Description

Cron-based scheduler inspired by [doctest](https://en.wikipedia.org/wiki/Doctest)

## Example

Cron jobs can be embedded into docstrings by using a [literal block](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks) (`::`). Literal blocks should start with `/etc/crontab`.

### Standard/Extended Format

Run `hello()` at every 2nd minute and 3rd minute:

```python
import time


def hello():
    """
    Print "hello world" at every 2nd minute and 3rd minute:

    /etc/crontab::

        */2 * * * *
        */3 * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "hello world")


if __name__ == '__main__':
    import doccron
    doccron.run_jobs()

```

### Quartz Format

Run `hello()` at every 2nd second and 3rd second:

```python
import time


def hello():
    """
    Print "hello world" every 2nd second and 3rd second:

    /etc/crontab::

        */2 * * * * *
        */3 * * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S'), "hello world")


if __name__ == '__main__':
    import doccron
    doccron.run_jobs(quartz=True)

```

### Timezone-Awareness (CRON_TZ)

DocCron now support `CRON_TZ`. The value of `CRON_TZ` only applies to succeeding cron jobs.
DocCron supports multiple `CRON_TZ` in a cron table. The default timezone value is the local/system timezone, if not specified. 

```python
import time


def hello():
    """
    Print "hello world" at every 2nd minute and 3rd minute:

    /etc/crontab::
    
        CRON_TZ=UTC
        */2 * * * *
        */3 * * * *
    """
    print(time.strftime('%Y-%m-%d %H:%M:%S%z'), "hello world")


if __name__ == '__main__':
    import doccron
    doccron.run_jobs()

```

## Features

- Standard and extended cron formats (see [CRON Expression](https://en.wikipedia.org/wiki/Cron#CRON_expression))
- [Nonstandard predefined scheduling definitions](https://en.wikipedia.org/wiki/Cron#Nonstandard_predefined_scheduling_definitions)
- [Non-standard characters](https://en.wikipedia.org/wiki/Cron#Non-standard_characters)
- [Quartz format](http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html)
- Works with documentation tools like [Sphinx](https://github.com/sphinx-doc/sphinx)
- Timezone-awareness (CRON_TZ)
- Interval (e.g., `@every 1h2m3s`)

## TODO

- Human-readable date/time strings 

## References

- [Cron Format](http://www.nncron.ru/help/EN/working/cron-format.htm)
- [Wikipedia - Cron](https://en.wikipedia.org/wiki/Cron)
- [cron library for Go](https://godoc.org/github.com/revel/cron)

## Author

- [Ronie Martinez](mailto:ronmarti18@gmail.com)
